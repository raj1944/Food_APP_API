from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    branches = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'user_id', 'restaurant_name', 'phone_no', 'city', 'address', 'branches')
      