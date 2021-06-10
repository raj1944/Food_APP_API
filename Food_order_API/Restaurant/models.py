from django.db import models
from User.models import User

# Create your models here.

class Restaurant(models.Model):
    user_id = models.IntegerField() 
    restaurant_name = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_name
        
	