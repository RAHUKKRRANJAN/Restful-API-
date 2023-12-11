from django.db import models
# from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# class Developer(models.Model):
#     client_id = models.CharField(max_length=100)
#     client_secret = models.CharField(max_length=100)
#    

# class YourAPI(models.Model):
#     # Define fields for your API
#     # name = models.CharField(max_length=100)
#       endpoint = models.CharField(max_length=100)
#     # Add other API-related fields