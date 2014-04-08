from voluptuous import Schema, All, Required, Match, MultipleInvalid
import bcrypt
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import hashlib
import datetime

from authentication import models
import meta.models
from errors import validators
from errors.exceptions import UserError

# Pseudo-function to trick makemessages into making message files
_ = lambda s: s

# Constants for use in authentication related script
SALT_ROUNDS = 13 # Number of Bcrypt salt rounds for encryption
INVALID_LOGIN = _('invalid-login') # Defined to provide ambiguous response
INVALID_RECOVERY = _('invalid-recovery')
INVALID_VALIDATION = _('invalid-validation')
TOKEN_SALT_SIZE = 64 # Token generator length
TOKEN_SIZE = 20
TOKEN_TIME = datetime.timedelta(days=30)
VALIDATION_TIME = datetime.timedelta(hours=5)

class User(object):
    """Provides wrapper method for handling users.
    
    Will return user instance based on values. Also handles creation
    of users and all validity checking. Basis for all authenticated
    operations of project.
    
    This class is allowed to be extensible beyond Django if efforts to
    migrate are made.
    """

    def __init__(self):
        # Establish docstring and add functions.

        self.user_obs = ()

    def get_user_objects(self):
        return self.user_obs

    def create(self, **user_info):
        """Creates user based on defined variables.
        
        Handles validation of credentials and creates database entry
        if validation succeeds. Does not create admin entries; admin
        entries are to be created by a different function to prevent
        accidental admin granting. Additional validation must also be
        employed. Also assigns user to instance if successful.
        
        Following are the info variables that may need to be
        defined prior to calling create. *s mean the variable is
        required:
        
        - username*
        - first_name
        - last_name
        - email*
        - password* (plaintext)
        - token - required if new-user setting is set to token

        TODO:
        MUST CHECK EXPIRATION ON TOKEN.
        """

        if self.user_obs:
            return self.user_obs

        errors = []
        validated = dict()
        token_required = False

        # Check to see if user creation is enabled
        new_users = meta.models.Data.objects.filter(tag='new-users')[0]

        if new_users.setting == 0:
            if new_users.data == 'token':
                token_required = True
            else:
                errors = (_('creation-disabled'),)
                raise UserError(errors)

        # Voluptuous schema for validation; tested with try statement
        schema_dict = {
            Required('username', _('username-required')): All(str,
                Match(validators.VALID_USERNAME_REGEX),
                msg=_('invalid-username')),
            'first_name': All(str, Match(validators.VALID_NAME_REGEX),
                msg=_('invalid-first-name')),
            'last_name': All(str, Match(validators.VALID_NAME_REGEX),
                msg=_('invalid-last-name')),
            Required('email', _('email-required')): All(str,
                Match(validators.VALID_EMAIL_REGEX),
                msg=_('invalid-email')),
            Required('password', _('password-required')): All(str,
                validators.Password, msg=_('invalid-password')),
        }

        if token_required:
            schema_dict[Required('token', _('token-required'))] = All(str,
                Match(validators.VALID_TOKEN_REGEX), msg=_('invalid-token'))

        schema = Schema(schema_dict)

        try:
            validated = schema(user_info)

            # Deletes user_info to get rid of sensitive data
            del user_info
        except MultipleInvalid as error:
            errors = validators.list_errors(error)

        if errors:
            raise UserError(errors)

        # Checks to see if token is in database if required
        if token_required:
            token_list = models.Tokens.objects.filter(
                purpose=models.TOKEN_NEW_USER, token=validated['token'])

            if len(token_list) != 1:
                errors = (_('no-such-token'),)
                raise UserError(errors)

            token_ob = token_list[0]

            if token_ob.exhausted:
                errors.append(_('token-exhausted'),)

            if token_ob.expired():
                errors.append(_('token-expired'),)

            if errors:
                raise UserError(tuple(errors))

            token_ob.exhausted = True
            token_ob.save()

            # Prevents entry of token into User object
            del validated['token']

        # Hashes password using bcrypt
        password = bcrypt.hashpw(validated['password'].encode('utf-8'),
            bcrypt.gensalt(SALT_ROUNDS))

        # Deletes password from info so it doesn't get inserted on creation
        del validated['password']

        current_user = models.Users.objects.filter(
            username__iexact=validated['username'])

        if current_user:
            errors = (_('user-exists'),)
            raise UserError(errors)

        current_email = models.Users.objects.filter(
            email__iexact=validated['email'])

        if current_email:
            errors = (_('email-exists'),)
            raise UserError(errors)

        # Saves user in user database
        user_ob = models.Users(**validated)
        user_ob.save()

        # Saves password in methods database
        pass_method = models.Methods()
        pass_method.user = user_ob
        pass_method.method = models.METHOD_PASSWORD
        pass_method.password = password
        pass_method.step = 1
        pass_method.save()

        # Creates and saves validation token
        random_salt = random_string(size=TOKEN_SALT_SIZE)
        email = validated['email']
        token = hashlib.sha1((email + random_salt).encode('utf-8')).hexdigest()

        token_method = models.Methods()
        token_method.user = user_ob
        token_method.method = models.METHOD_VALIDATION_TOKEN
        token_method.token = token
        token_method.step = 0
        token_method.save()

        # Emails user; may use template for email in future
        subject = 'Account Validation'
        text = 'Your validation token is:\n%s' % token

        try:
            send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
        except:
            errors = (_('validation-email-failure'),)
            raise UserError(errors)

        self.user_obs = [user_ob]

        return self.user_obs

    def login_password(self, **user_info):
        """Handler to login via password authentication.
        
        Accepts two pieces of information: username and password. Both
        are required. Validates, checks and returns user object if user
        exists and password is correct.
        
        TODO:
        MUST ASSIGN SESSIONS.
        MUST UPDATE ACCESS TIME (SESSIONS MAY DO THIS).
        """

        if self.user_obs:
            return self.user_obs

        errors = []
        validated = dict()

        # Check to see if user login is enabled
        new_users = meta.models.Data.objects.filter(tag='user-login')[0]

        if new_users.setting == 0:
            errors = (_('login-disabled'),)
            raise UserError(errors)

        # Voluptuous schema for validation; tested with try statement
        schema = Schema({
            Required('username', _('username-required')): All(str,
                msg=_('invalid-username')),
            Required('password', _('password-required')): All(str,
                msg=_('invalid-password')),
        })

        try:
            validated = schema(user_info)

            # Deletes user_info to get rid of sensitive data
            del user_info
        except MultipleInvalid as error:
            errors = validators.list_errors(error)

        if errors:
            raise UserError(errors)

        try:
            user_ob = models.Users.objects.get(
                username__iexact=validated['username'])
        except models.Users.DoesNotExist:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)

        if not user_ob.active:
            return _('user-inactive'), INVALID_LOGIN,

        try:
            method = models.Methods.objects.get(user=user_ob,
                method=models.METHOD_PASSWORD, step=1,
                status=models.METHOD_ACTIVE)
        except models.Methods.DoesNotExist:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)

        password_hash = method.password.encode('utf-8')
        password = bcrypt.hashpw(validated['password'].encode('utf-8'),
                                 password_hash)

        # Deletes original password to prevent later misuse
        del validated['password']

        if password != password_hash:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)

        self.user_obs = [user_ob]

        return self.user_obs

    def get_by_info(self, multiple=False, **user_info):
        """Retrieves user object found by given data.
        
        Assigns to user_obs.
        If multiple is true, assigns multiple selections. Limits to one
        otherwise.
        All other keywords passed directly to model filter.
        """

        if self.user_obs:
            return self.user_obs

        errors = []

        user_list = models.Users.objects.filter(**user_info)

        if not multiple:
            if len(user_list) > 1:
                errors = (_('multiple-results'),)
                raise UserError('multiple-results')

        if not user_list:
            errors = (_('no-results'),)
            raise UserError(errors)

        self.user_obs = user_list

        return self.user_obs

    def delete(self):
        """Deletes users in user_obs.
        
        Use cautiously, and only for cron cleanups or admin removals.
        All related data must be archived before running this command,
        with an exception for methods, which will be cascaded.
        """

        if not self.user_obs:
            return False

        errors = []

        for user_ob in self.user_obs:
            try:
                user_ob.delete()
            except models.Users.ProtectedError:
                errors = (_('associated-data-present'))
                raise UserError(errors)

        return True

    def deactivate(self):
        """Preferred method for "deletion." Sets user to deactivated.
        
        Also deactivates all methods.
        
        This may be paired with a cron job to automatically delete
        users after being deactivated for a certain amount of time.
        Cron job may also remove user after archiving data. Locks user
        out of recreation for the time being.
        
        For now, all deactivated accounts remain deactivated.
        """

        if not self.user_obs:
            return False

        errors = []

        for user_ob in self.user_obs:
            user_ob.active = False
            user_ob.save()

            method_list = models.Methods.objects.filter(user=user_ob)
            method_list.update(status=models.METHOD_INACTIVE)

        return True

    def activate(self):
        """Merely opposite of deactivate. Refer to deactivate."""

        if not self.user_obs:
            return False

        errors = []

        for user_ob in self.user_obs:
            user_ob.active = False
            user_ob.save()

            method_list = models.Methods.objects.filter(user=user_ob)
            method_list.update(status=models.METHOD_ACTIVE)

        return True

    def set_type(self, user_type):
        """Sets type of user. Recommended to use constants in model."""

        if not self.user_obs:
            return False

        errors = []

        for user_ob in self.user_obs:
            user_ob.user_type = user_type

        return True

    def modify_info(self, **user_info):
        """Modifies user information for users.
        
        Note that this only allows modification of user details, such
        as username, names and email. It does not allow modification of
        settings such as user_type. For that, specific functions must
        be used.
        """

        if not self.user_obs:
            return False

        errors = []
        validated = dict()

        schema = Schema({
            'username': All(str, Match(validators.VALID_USERNAME_REGEX),
                msg=_('invalid-username')),
            'first_name': All(str, Match(validators.VALID_NAME_REGEX),
                msg=_('invalid-first-name')),
            'last_name': All(str, Match(validators.VALID_NAME_REGEX),
                msg=_('invalid-last-name')),
            'email': All(str, Match(validators.VALID_EMAIL_REGEX),
                msg=_('invalid-email')),
        })

        try:
            validated = schema(user_info)
        except MultipleInvalid as error:
            errors = validators.list_errors(error)

        if errors:
            raise UserError(errors)

        for user_ob in self.user_obs:
            # Creates new queryset to update data, since model
            # model instances cannot handle it on their own
            user_queryset = models.Users.objects.get(pk=user_ob.pk)
            user_queryset.update(**validated)

        return True

    def modify_password(self, new, check=True, old=None):
        """Optionally checks and sets password for single user."""

        if len(self.user_obs) != 1:
            return False

        errors = []

        schema = Schema({
            Required('password', _('password-required')): All(str,
                msg=_('invalid-password')),
        })

        try:
            schema({'password': new})
        except MultipleInvalid as error:
            errors = validators.list_errors(error)

        user_ob = self.user_obs[1]

        method = models.Methods.get(user=user_ob,
            method=models.METHOD_PASSWORD)

        if check:
            if not old:
                return False

            password_hash = method.password.encode('utf-8')
            password = bcrypt.hashpw(old.encode('utf-8'), password_hash)

            del old

            if password != password_hash:
                return False

        password = bcrypt.hashpw(old.encode('utf-8'),
            bcrypt.gensalt(SALT_ROUNDS))

        method.password = password

    def recover_account(self):
        """Creates recovery email token and sends it to user.

        TODO:
        EXPIRATION DATE
        """

        if len(self.user_obs) != 1:
            return False

        errors = []

        user_ob = self.user_obs[0]

        models.Methods.objects.filter(user=user_ob,
            method=models.METHOD_RECOVERY_TOKEN,
            status=models.METHOD_ACTIVE).update(status=models.METHOD_INACTIVE)

        email = user_ob.email
        random_salt = random_string(size=TOKEN_SALT_SIZE)
        token = hashlib.sha1((email + random_salt).encode('utf-8')).hexdigest()

        method = models.Methods()
        method.user = user_ob
        method.method = models.METHOD_RECOVERY_TOKEN
        method.token = token
        method.step = 0
        method.expiration = datetime.datetime.now() + VALIDATION_TIME
        method.save()

        subject = 'Recovery Token'
        text = 'Your account recovery token is: %s' % token

        try:
            send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
        except:
            errors = (_('recovery-email-failure'),)
            raise UserError(errors)

        return True

    def login_recovery(self, **user_info):
        """Validates recovery email token against methods."""

        if self.user_obs:
            return self.user_obs

        schema = Schema({
            Required('username', _('username-required')): All(str,
                msg=_('invalid-username')),
            Required('token', _('token-required')): All(str,
                Match(validators.VALID_TOKEN_REGEX), msg=_('invalid-token'))
        })

        try:
            validated = schema(user_info)

            del user_info
        except MultipleInvalid as error:
            errors = validators.list_errors(error)
            raise UserError(errors)

        try:
            user_ob = models.Users.objects.get(username=validated['username'],
                active=True)
        except models.Users.DoesNotExist:
            errors = (INVALID_RECOVERY,)
            raise UserError(errors)

        try:
            method = models.Methods.objects.get(user=user_ob,
                method=models.METHOD_RECOVERY_TOKEN,
                status=models.METHOD_ACTIVE)
        except models.Methods.DoesNotExist:
            errors = (INVALID_RECOVERY,)
            raise UserError(errors)

        method.status = models.METHOD_INACTIVE
        method.save()

        if method.expired():
            errors = (INVALID_RECOVERY,)
            raise UserError(errors)

        self.user_obs = (user_ob,)
        return self.user_obs

    def validate_account(self, **user_info):
        """Validates account based on emailed token."""

        if self.user_obs:
            return False

        schema = Schema({
            Required('username', _('username-required')): All(str,
                msg=_('invalid-username')),
            Required('token', _('token-required')): All(str,
                Match(validators.VALID_TOKEN_REGEX), msg=_('invalid-token'))
        })

        try:
            validated = schema(user_info)

            del user_info
        except MultipleInvalid as error:
            errors = validators.list_errors(error)
            raise UserError(errors)

        try:
            user_ob = models.Users.objects.get(username=validated['username'],
                active=True)
        except models.Users.DoesNotExist:
            errors = (INVALID_VALIDATION,)
            raise UserError(errors)

        try:
            method = models.Methods.objects.get(user=user_ob,
                method=models.METHOD_VALIDATION_TOKEN,
                status=models.METHOD_ACTIVE)
        except models.Methods.DoesNotExist:
            errors = (INVALID_VALIDATION,)
            raise UserError(errors)

        method.status = models.METHOD_INACTIVE
        method.save()

        if method.expired():
            errors = (INVALID_VALIDATION,)
            raise UserError(errors)

        return True

def random_string(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def generate_token(purpose, expiration_delta=TOKEN_TIME):
    """Generates token for given purpose and adds it to database."""

    token = random_string(size=TOKEN_SIZE)

    token_ob = models.Tokens()
    token_ob.purpose = purpose
    token_ob.token = token
    token_ob.expiration = expiration_delta
    token_ob.save()

    return True

def modify_meta_data(tag, setting=None, data=None):
    """Modifies meta data in meta app."""

    if not setting and not data:
        return False

    meta_ob = meta.models.Data.objects.get(tag=tag)

    if setting:
        meta_ob.setting = setting

    if data:
        meta_ob.data = data

    return False