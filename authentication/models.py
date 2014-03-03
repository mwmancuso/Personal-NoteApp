from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=50)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(max_length=75)
	password = models.CharField(max_length=60)
	password_updated = models.DateTimeField(auto_now_add=True)
	passwords_previous = models.TextField(blank=True)
	user_type = models.IntegerField(default=0)
	last_access = models.DateTimeField()
	user_created = models.DateTimeField(auto_now_add=True)
	user_modified = models.DateTimeField(auto_now=True, auto_now_add=True)