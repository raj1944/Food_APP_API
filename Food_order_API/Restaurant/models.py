from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    address =models.CharField(max_length=100)
    restaurant_id = models.IntegerField(default=0,blank=True)
    branch_id = models.IntegerField(default=0,blank=True)

class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=60)
    owner_name = models.CharField(max_length=60)

    def __str__(self):
        return self.restaurant_name

class Branches(models.Model):
    restaurant = models.ForeignKey(Restaurants, related_name='branches', on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=60)
    manager_name = models.CharField(max_length=60)

    def __str__(self):
        return self.branch_name

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.food_name

class Menu(models.Model):
    food  = models.ForeignKey(Food,related_name='menu', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches,related_name='menu', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.food.food_name+' - '+str(self.price)

class Order(models.Model):
    total_amount = models.IntegerField(default=0)
    delivery_addr = models.CharField(max_length=50,blank=True)
    user_id = models.ForeignKey(User ,on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branches, related_name='order', on_delete=models.CASCADE)


class orderItem(models.Model):
    menu_id = models.ForeignKey(Menu, related_name='orderitem', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
	