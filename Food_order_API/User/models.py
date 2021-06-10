from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100) 