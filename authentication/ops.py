from authentication.models import Users, Methods
import strings
import re

# Validation constants
# Note: tuples for length contain a low and high value
VALID_USERNAME_CHARS = set(string.ascii_lowercase, '_')
VALID_NAME_CHARS = set(string.ascii_lowercase)
VALID_PASS_SYMBOLS = set(string.punctuation + ' ')
VALID_PASS_CHARS = set(string.digits + string.ascii_lowercase\
                       + string.ascii_uppercase + VALID_PASS_SYMBOLS)
VALID_EMAIL_REGEX = re.compile('[^@]+@[^@]+\.[^@]+')
VALID_USERNAME_LEN = (1, Users._meta.get_field('username').max_length)
VALID_FIRST_NAME_LEN = (1, Users._meta.get_field('first_name').max_length)
VALID_LAST_NAME_LEN = (1, Users._meta.get_field('last_name').max_length)
VALID_EMAIL_LEN = (1, Users._meta.get_field('email').max_length)
VALID_PASS_LEN = (8, 72)

class User(object):
    """Provides wrapper method for handling users.
    
    Will return user instance based on values. Also handles creation
    of users and all validity checking. Basis for all authenticated
    operations of project.
    
    This class is allowed to be extensible beyond Django if efforts to
    migrate are made.
    """
    
    def __init__(self, exists=True):
        # Establish docstring and add functions.
        self.exists = exists
        
        # Establish instance variables
        self.username = ''
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.password = ''
        
        if self.exists:
            pass
        else:
            pass
    
    def create(self):
        """Creates user based on defined variables.
        
        Handles validation of credentials and creates database entry
        if validation succeeds. Does not create admin entries; admin
        entries are to be created by a different function to prevent
        accidental admin granting. Additional validation must also be
        employed. Also assigns user to instance if successful.
        
        Following are the instance variables that may need to be
        defined prior to calling create. *s mean the variable is
        required:
        
        - username*
        - first_name
        - last_name
        - email*
        - password* (plaintext)
        """
        
        if self.exists:
            # RAISES ERROR #
            return
        
        # Validations
        if not self.username:
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('no username')
        
        if not self.email:
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('no email')
        
        if not self.password:
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('no password')
        
        if not all(char in VALID_USERNAME_CHARS for char in self.username):
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('invalid characters in username')
        
        if self.username.len < VALID_USERNAME_LEN[0]\
                or self.username.len > VALID_USERNAME_LEN[1]:
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('invalid number of characters in username')
        
        if not all(char in VALID_NAME_CHARS for char in self.first_name):
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('invalid characters in first_name')
        
        if self.first_name.len < VALID_FIRST_NAME_LEN[0]\
                or self.first_name.len > VALID_USERNAME_LEN[1]:
            # NEEDS ERROR HANDLER #
            self.validation_errors.append('invalid number of characters in username')