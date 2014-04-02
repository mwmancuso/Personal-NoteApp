from authentication import models
from meta.models import Data
from errors import validators
from errors.exceptions import UserError
from voluptuous import Schema, All, Required, Match, MultipleInvalid, Msg,\
                       IsFalse, Lower
import bcrypt
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from hashlib import sha1

# Pseudo-function to trick makemessages into making message files
_ = lambda s: s

# Constants for use in authentication related script
SALT_ROUNDS = 13 # Number of Bcrypt salt rounds for encryption
INVALID_LOGIN = _('invalid-login') # Defined to provide ambiguous response

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
        
        self.user_ob = None
    
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
        """
        
        if self.user_ob:
            return self.user_ob
        
        errors = []
        token_required = False
        
        # Check to see if user creation is enabled
        new_users = Data.objects.filter(tag='new-users')[0]
        
        if new_users.setting == 0:
            if new_users.data == 'token':
                token_required = True
            else:
                errors = (_('creation-disabled'),)
                raise UserError(errors)
        
        # Voluptuous schema for validation; tested with try statement
        schema_dict = {
            Required('username', _('username-required')): All(str,\
                Match(validators.VALID_USERNAME_REGEX),\
                msg=_('invalid-username')),
            'first_name': All(str, Match(validators.VALID_NAME_REGEX),\
                msg=_('invalid-first-name')),
            'last_name': All(str, Match(validators.VALID_NAME_REGEX),\
                msg=_('invalid-last-name')),
            Required('email', _('email-required')): All(str,\
                Match(validators.VALID_EMAIL_REGEX),\
                msg=_('invalid-email')),
            Required('password', _('password-required')): All(str,\
                validators.Password, msg=_('invalid-password')),
        }
        
        if token_required:
            schema_dict[Required('token', _('token-required'))] = All(str,\
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
            token_list = models.Tokens.objects.filter(\
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
        password = bcrypt.hashpw(validated['password'].encode('utf-8'),\
            bcrypt.gensalt(SALT_ROUNDS))
        
        # Deletes password from info so it doesn't get inserted on creation
        del validated['password']
        
        current_user = models.Users.objects.filter(\
            username__iexact=validated['username'])
        
        if current_user:
            errors = (_('user-exists'),)
            raise UserError(errors)
        
        current_email = models.Users.objects.filter(\
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
        random = random_string(size=32)
        email = validated['email']
        token = sha1((email + random).encode('utf-8')).hexdigest()
        
        token_method = models.Methods()
        token_method.user = user_ob
        token_method.method = models.METHOD_VALIDATION_TOKEN
        token_method.token = token
        token_method.step = 0
        token_method.save()
        
        # Emails user; may use template for email in future
        subject = 'Account Validation'
        text = 'Your validation token is:\n%s' % (token)
        
        try:
            send_mail(subject, text, settings.EMAIL_HOST_USER, [email])
        except:
            errors = (_('validation-email-failure'),)
            raise UserError(errors)
        
        self.user_ob = user_ob
        
        return self.user_ob
    
    def login_password(self, **user_info):
        """Handler to login via password authentication.
        
        Accepts two pieces of information: username and password. Both
        are required. Validates, checks and returns user object if user
        exists and password is correct.
        
        TODO:
        MUST ASSIGN SESSIONS.
        """
        
        if self.user_ob:
            return self.user_ob
        
        errors = []
        
        # Check to see if user login is enabled
        new_users = Data.objects.filter(tag='user-login')[0]
        
        if new_users.setting == 0:
            errors = (_('login-disabled'),)
            raise UserError(errors)
        
        # Voluptuous schema for validation; tested with try statement
        schema = Schema({
            Required('username', _('username-required')): All(str,\
                msg=_('invalid-username')),
            Required('password', _('password-required')): All(str,\
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
        
        user_list = models.Users.objects.filter(\
            username__iexact=validated['username'])
        
        if not user_list:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)
            # May implement delay here to prevent username extracting
        elif len(user_list) != 1:
            # May cause another error here; only one response should be
            # returned.
            errors = (INVALID_LOGIN,)
            raise UserError(errors)
        
        user_ob = user_list[0]
        
        if not user_ob.active:
            return (_('user-inactive'), INVALID_LOGIN,)
        
        method_list = models.Methods.objects.filter(user=user_ob,\
            method=models.METHOD_PASSWORD, step=1,\
            status=models.METHOD_ACTIVE)
        
        if not method_list:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)
        elif len(method_list) != 1:
            # May implement error or other handler to handle multiple
            # passwords.
            errors = (INVALID_LOGIN,)
            raise UserError(errors)
        
        methods = method_list[0]
        
        hash = methods.password.encode('utf-8')
        password = bcrypt.hashpw(validated['password'].encode('utf-8'), hash)
        
        # Deletes original password to prevent later misuse
        del validated['password']
        
        if password != hash:
            errors = (INVALID_LOGIN,)
            raise UserError(errors)
        
        self.user_ob = user_ob
        
        return self.user_ob
    
    def get_by_info(self, **user_info):
        pass
    
    def delete(self):
        pass
    
    def modify_info(self, **user_info):
        pass
    
    def modify_password(self, **user_info):
        pass
    
    def recover_account(self):
        pass
    
    def validate_recovery(self, recovery_key):
        pass
    

def random_string(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def generate_token():
    pass

def modify_meta_data():
    pass