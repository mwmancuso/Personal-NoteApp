from django.db import models

DEFAULT_DATA = {
    'new-users': {
        # 1 for yes, 0 for no
        'setting': 1,
        # If no, empty for no token and "token" for token creation
        'data': '',
    },
    'user-login': {
        # 1 for yes, 0 for no
        'setting': 1,
        'data': '',
    },
}

class DataManager(models.Manager):
    """Manager for meta-data class."""
    
    def populate(self):
        """Populates database with data given in DEFAULT_DATA."""
        
        for tag in DEFAULT_DATA.keys():
            self.get_or_create(tag=tag, defaults=DEFAULT_DATA[tag])


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
    setting = models.IntegerField(null=True)
    data = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    # Replaces default manager with custom one
    objects = DataManager()
    
    def __str__(self):
        return self.tag