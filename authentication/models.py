from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=75)
    user_type = models.IntegerField(default=0)
    last_access = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.username

class Methods(models.Model):
    user_id = models.ForeignKey(Users)
    method = models.IntegerField()
    password = models.CharField(max_length=60, blank=True)
    token = models.TextField(blank=True)
    step = models.IntegerField()
    status = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.user_id