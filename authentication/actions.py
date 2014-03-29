from authentication import models
from errors import validators
from errors.exceptions import UserError
from voluptuous import Schema, All, Required, Match, MultipleInvalid, Msg,\
                       IsFalse, Lower
import bcrypt
from django.db.models import Q

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
        self.methods = None
    
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
        
        TODO:
        MUST CREATE EMAIL SYSTEM FOR VALIDATIONS.
        """
        
        if self.user_ob:
            raise RuntimeError('The user already exists.')
        
        errors = ()
        
        # Voluptuous schema for validation; tested with try statement
        schema = Schema({
            Required('username', _('username-required')): All(str, Lower,\
                Match(validators.VALID_USERNAME_REGEX),\
                msg=_('invalid-username')),
            'first_name': All(str, Match(validators.VALID_NAME_REGEX),\
                msg=_('invalid-first-name')),
            'last_name': All(str, Match(validators.VALID_NAME_REGEX),\
                msg=_('invalid-last-name')),
            Required('email', _('email-required')): All(str, Lower,\
                Match(validators.VALID_EMAIL_REGEX),\
                msg=_('invalid-email')),
            Required('password', _('password-required')): All(str,\
                validators.Password, msg=_('invalid-password')),
        })
        
        try:
            validated = schema(user_info)
            
            # Deletes user_info to get rid of sensitive data
            del user_info
        except MultipleInvalid as error:
            errors = validators.list_errors(error)
        
        if errors:
            raise UserError(errors)
        
        # Hashes password using bcrypt
        password = bcrypt.hashpw(validated['password'].encode('utf-8'),\
            bcrypt.gensalt(SALT_ROUNDS))
        
        # Deletes password from info so it doesn't get inserted here
        del validated['password']
        
        current_user = models.Users.objects.filter(\
            username = validated['username'])
        
        if current_user:
            errors = (_('user-exists'),)
            raise UserError(errors)
        
        current_email = models.Users.objects.filter(\
            email = validated['email'])
        
        if current_email:
            errors = (_('email-exists'),)
            raise UserError(errors)
        
        user_ob = models.Users(**validated)
        
        user_ob.save()
        
        methods = models.Methods()
        
        methods.user = self.user_ob
        methods.method = models.METHOD_PASSWORD
        methods.password = password
        methods.step = 1
        
        methods.save()
        
        self.user_ob = user_ob
        self.methods = methods
        
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
            raise RuntimeError('The user already exists.')
        
        errors = ()
        
        # Voluptuous schema for validation; tested with try statement
        schema = Schema({
            Required('username', _('username-required')): All(str, Lower,\
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
            username=validated['username'])
        
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
        
        if user_ob.user_type == models.USER_INACTIVE:
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
        self.methods = methods
        
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