from rest_framework import serializers
from .models import Order, Order_Item
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = "__all__"
