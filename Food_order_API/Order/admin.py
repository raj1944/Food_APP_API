from django.contrib import admin
from .models import Order, orderItem

# Register your models here.
admin.site.register(Order)
admin.site.register(orderItem)