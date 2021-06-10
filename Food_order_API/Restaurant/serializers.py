from rest_framework import serializers
from .models import Restaurants, Branches, Food, Menu, Order, orderItem, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'address')

class RestaurantsSerializer(serializers.ModelSerializer):
    branches = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Restaurants
        fields = ('id', 'restaurant_name', 'owner_name', 'branches')

class BranchesSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurants.objects.all(), many=False)
    menu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   
    class Meta:
        model = Branches
        fields = ('id', 'branch_name', 'manager_name', 'restaurant', 'menu')

class FoodSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   
    class Meta:
        model = Food
        fields = ('id', 'food_name', 'category', 'menu')

class MenuSerializer(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), many=False)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branches.objects.all(), many=False)   
    class Meta:
        model = Menu
        fields = ('id', 'food', 'branch', 'price', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branches.objects.all(), many=False)
    orderitem = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'total_amount', 'delivery_addr', 'user_id', 'branch_id', 'orderitem')

class orderItemSerializer(serializers.ModelSerializer):
    menu_id = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), many=False)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=False)   
    class Meta:
        model = orderItem
        fields = ('id', 'menu_id', 'order_id', 'quantity', 'total_price')        


