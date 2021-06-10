from django.db import models
from Restaurant.models import Restaurant
from User.models import User
# Create your models here.

class Branch(models.Model):
    user_id = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, related_name='branches', on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name