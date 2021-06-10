from rest_framework import serializers
from .models import Branch
from Restaurant.models import Restaurant

class BranchSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), many=False)
    menu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   
    class Meta:
        model = Branch
        fields = ('id', 'user_id', 'branch_name', 'restaurant', 'phone_no', 'city', 'menu')