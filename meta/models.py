from django.db import models

class Data(models.Model):
    """Model for meta-data. Needed for system-wide key/value pairs.
    
    setting field is for simple numerical values.
    data field is for extra data.
    
    Current tags:
    new-users:
        1: yes
        0: no
    user-login:
        1: yes
        0: no
    """
    
    tag = models.CharField(max_length=30, unique=True)
    setting = models.IntegerField(blank=True)
    data = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.tag