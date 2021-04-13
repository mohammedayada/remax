from django.shortcuts import render
from .serializer import (
    OrderSerializer,
    OrderItemSerializer,
    Order,
    Order_Item
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderItemSerializer
    queryset = Order_Item.objects.all()

