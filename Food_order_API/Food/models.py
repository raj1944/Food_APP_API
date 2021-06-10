from django.db import models
from Branch.models import Branch
# Create your models here.

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.food_name

class Menu(models.Model):
    food  = models.ForeignKey(Food,related_name='menu', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,related_name='menu', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.food.food_name+' - '+str(self.price)