from django.db import models
from Food.models import Menu
from User.models import User
from Branch.models import Branch 
# Create your models here.

class Order(models.Model):
    total_amount = models.IntegerField(default=0)
    delivery_addr = models.CharField(max_length=50,blank=True)
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, related_name='order', on_delete=models.CASCADE)


class orderItem(models.Model):
    menu_id = models.ForeignKey(Menu, related_name='orderitem', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
