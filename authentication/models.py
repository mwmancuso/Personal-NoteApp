from django.db import models
import pytz
import smtplib
from voluptuous import Schema, All, Required, Match, MultipleInvalid
import bcrypt
from django.core.mail import send_mail
from django.conf import settings
import hashlib
import datetime
import logging

import meta.models
from errors import validators
from errors.exceptions import UserError
from authentication.helpers import random_string

logger = logging.getLogger(__name__)

# Pseudo-function to trick makemessages into making message files
_ = lambda s: s

# Static variables for clarity in database
USER_STANDARD = 0
USER_ADMIN = 1
METHOD_PASSWORD = 0
METHOD_VALIDATION_TOKEN = 1
METHOD_RECOVERY_TOKEN = 2
METHOD_ACTIVE = 1
METHOD_INACTIVE = 0
TOKEN_NEW_USER = 'new-user'

# Constants for use in authentication related script
SALT_ROUNDS = 13 # Number of Bcrypt salt rounds for encryption
INVALID_LOGIN = _('invalid-login') # Defined to provide ambiguous response
INVALID_RECOVERY = _('invalid-recovery')
INVALID_VALIDATION = _('invalid-validation')
TOKEN_SALT_SIZE = 64 # Token generator length
TOKEN_SIZE = 20
TOKEN_TIME = datetime.timedelta(days=30)
VALIDATION_TIME = datetime.timedelta(hours=5)

class UserManager(models.Manager):
    """Define this."""

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
        """

        user_errors = []
        token_required = False
        token_object = None

        # Check to see if user creation is enabled
        new_users = meta.models.Data.objects.get(tag='new-users')

        if new_users.setting == 0:
            if new_users.data == 'token':
                token_required = True
            else:
                user_errors.append(_('creation-disabled'))
                raise UserError(*user_errors)

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

        # Adds required key to schema if token is required
        if token_required:
            schema_dict[Required('token', _('token-required'))] = All(str,
                Match(validators.VALID_TOKEN_REGEX), msg=_('invalid-token'))

        schema = Schema(schema_dict)

        try:
            validated = schema(user_info)

            # Deletes user_info to get rid of sensitive data
            del user_info
        except MultipleInvalid as error:
            if error.error_message == 'extra keys not allowed':
                raise

            user_errors = validators.list_errors(error)
            raise UserError(*user_errors)

        # Checks to see if token is in database if required
        if token_required:
            try:
                token_object = Tokens.objects.get(
                    purpose=TOKEN_NEW_USER, token=validated['token'])
            except Tokens.DoesNotExist:
                user_errors.append(_('no-such-token'))
                raise UserError(*user_errors)

            if token_object.exhausted:
                user_errors.append(_('token-exhausted'))

            if token_object.expired():
                user_errors.append(_('token-expired'))

            if user_errors:
                raise UserError(*user_errors)

            token_object.exhausted = True

            # Prevents entry of token into User object
            del validated['token']

        # Hashes password using bcrypt
        encrypted_password = bcrypt.hashpw(validated['password'].encode('utf-8'),
            bcrypt.gensalt(SALT_ROUNDS))

        # Deletes password from info so it doesn't get inserted on creation
        del validated['password']

        current_user = self.get_queryset().filter(
            username__iexact=validated['username'])

        if current_user:
            user_errors.append(_('user-exists'))
            raise UserError(*user_errors)

        current_email = self.get_queryset().filter(email__iexact=validated[
            'email'])

        if current_email:
            user_errors.append(_('email-exists'))
            raise UserError(*user_errors)

        # Sets instance variables to those of the validated dictionary
        # for key, value in list(validated.items()):
        #     setattr(self, key, value)

        # Saves password in methods database
        password_method = Methods()
        password_method.method = METHOD_PASSWORD
        password_method.password = encrypted_password
        password_method.step = 1

        # Creates and saves validation token
        random_salt = random_string(size=TOKEN_SALT_SIZE)
        email = validated['email']
        token = hashlib.sha1((email + random_salt).encode('utf-8')).hexdigest()

        validation_token_method = Methods()
        validation_token_method.method = METHOD_VALIDATION_TOKEN
        validation_token_method.token = token
        validation_token_method.step = 0

        # Saves all data if validation was complete
        if token_required:
            token_object.save()
        user_object = self.get_queryset().create(**validated)
        password_method.user = user_object
        password_method.save()
        validation_token_method.user = user_object
        validation_token_method.save()

        # Emails user; may use template for email in future
        subject = 'Account Validation'
        text = 'Your validation token is:\n%s' % token

        try:
            send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
        except smtplib.SMTPException as error:
            logger.exception(error)

            user_errors.append(_('validation-email-failure'))
            raise UserError(*user_errors)

        return user_object

class Users(models.Model):
    """Database model for user storage.
    
    Does not store user authentication methods. Fields requiring
    further explanation are as follows:
    
    user_type: integer describing the type of user. As of now, includes
            the following:
        0: standard user
        1: admin user
    """

    objects = UserManager()
    users = objects

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=75)
    user_type = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    last_access = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    validated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

    def login_password(self, **user_info):
        """Handler to login via password authentication.

        Accepts two pieces of information: username and password. Both
        are required. Validates, checks and returns user object if user
        exists and password is correct.

        TODO:
        MUST ASSIGN SESSIONS.
        MUST UPDATE ACCESS TIME (SESSIONS MAY DO THIS).
        """

        if self.username:
            raise RuntimeError('A user is assigned to this instance.')

        errors = []

        # Check to see if user login is enabled
        user_login = meta.models.Data.objects.get(tag='user-login')

        if user_login.setting == 0:
            errors.append(_('login-disabled'))
            raise UserError(*errors)

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
            if error.error_message == 'extra keys not allowed':
                raise

            errors = validators.list_errors(error)
            raise UserError(*errors)

        try:
            user_ob = Users.objects.get(
                username__iexact=validated['username'])
        except Users.DoesNotExist:
            errors.append(INVALID_LOGIN)
            raise UserError(*errors)

        if not user_ob.active:
            errors.append(_('user-inactive'))
            errors.append(INVALID_LOGIN)
            raise UserError(*errors)

        try:
            method = Methods.objects.get(user=user_ob,
                method=METHOD_PASSWORD, step=1,
                status=METHOD_ACTIVE)
        except Methods.DoesNotExist:
            errors.append(INVALID_LOGIN)
            raise UserError(*errors)

        password_hash = method.password.encode('utf-8')
        password = bcrypt.hashpw(validated['password'].encode('utf-8'),
                                 password_hash)

        # Deletes original password to prevent later misuse
        del validated['password']

        if password != password_hash:
            errors.append(INVALID_LOGIN)
            raise UserError(*errors)

        return True

class Methods(models.Model):
    """Database model for authentication methods. Fields requiring
    further explanation are as follows:
    
    method: integer representing method type:
        0: password
        1: validation token
    password/token: only one may be defined; password hashes are often
            shorter and quicker and are not arbitrary.
    step: for multi-step authentication, important to be defined.
        Numbered by number of step, i.e. 1 for first step.
    status: current availability status of the method for the user.
            Currently includes the following:
        1: active
        0: inactive
    """
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    method = models.IntegerField()
    password = models.CharField(max_length=60, blank=True)
    token = models.TextField(blank=True)
    step = models.IntegerField()
    status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    last_used = models.DateTimeField(null=True)
    expiration = models.DateTimeField(null=True)

    def expired(self):
        """Checks to see if method has been expired yet."""

        # Returns true if no expiration date
        if not self.expiration:
            return False

        return datetime.datetime.now(pytz.utc) > self.expiration
    
    def __str__(self):
        return str(self.method)

class Tokens(models.Model):
    """Model for tokens used throughout project.

    This model is not intended for individual tokens, i.e., email
    validation tokens. It is meant for system-wide tokens.

    Tokens must be either letters or numbers, that's it.
    """
    
    purpose = models.CharField(max_length=30)
    token = models.CharField(max_length=50, unique=True)
    exhausted = models.BooleanField(default=False)
    expiration = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    # Defines helper functions

    def expired(self):
        """Checks to see if token has been expired or not."""

        # Returns not expired if no expiration date
        if not self.expiration:
            return False
        
        return datetime.datetime.now(pytz.utc) > self.expiration

    # Defines authentication methods

    def __str__(self):
        return self.purpose