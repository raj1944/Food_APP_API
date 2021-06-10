from rest_framework import serializers
from .models import Food, Menu
from Branch.models import Branch

class FoodSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   
    class Meta:
        model = Food
        fields = ('id', 'food_name', 'category', 'menu')

class MenuSerializer(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), many=False)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=False)   
    class Meta:
        model = Menu
        fields = ('id', 'food', 'branch', 'price', 'quantity')