from django.db import models

# Static variables for clarity in database
METHOD_PASSWORD = 0
METHOD_VALIDATION_TOKEN = 1
METHOD_ACTIVE = 0
METHOD_INACTIVE = 1
USER_VALIDATED = 1
USER_NOT_VALIDATED = 0

class Users(models.Model):
    """Database model for user storage.
    
    Does not store user authentication methods. Fields requiring
    further explanation are as follows:
    
    user_type: integer describing the type of user. As of now, includes
            the following:
        0: standard user
        1: admin user
    """
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=75)
    user_type = models.IntegerField(default=0)
    last_access = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    validated = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username

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
        0: active
        1: inactive
    """
    user = models.ForeignKey(Users)
    method = models.IntegerField()
    password = models.CharField(max_length=60, blank=True)
    token = models.TextField(blank=True)
    step = models.IntegerField()
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    last_used = models.DateTimeField(null=True)
    
    def __str__(self):
        return str(self.method)