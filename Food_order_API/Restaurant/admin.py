from django.contrib import admin

# Register your models here.
from .models import Restaurants, Branches, Food, Menu, Order, orderItem, User
admin.site.register(Restaurants)
admin.site.register(Branches)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(User)