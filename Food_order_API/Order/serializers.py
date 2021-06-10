from rest_framework import serializers
from .models import Order, orderItem
from Food.models import Menu
from Branch.models import Branch

class OrderSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), many=False)
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