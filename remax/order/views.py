from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import (
    OrderSerializer,
    OrderItemSerializer,
    Order,
    Order_Item
)


# To get all Orders
class OrderGetList(APIView):
    """
    List all Orders.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


# To post Orders
class OrderPostList(APIView):
    """
    Create a new Order.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Order instance.
class OrderDetail(APIView):
    """
    Retrieve, update or delete a Order instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get all Order Items
class OrderItemGetList(APIView):
    """
    List all Order Item.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        order_items = Order_Item.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)


# To post Order Item
class OrderItemPostList(APIView):
    """
    Create a new Order Item.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Order Item instance.
class OrderItemDetail(APIView):
    """
    Retrieve, update or delete a Order Item instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order_Item.objects.get(pk=pk)
        except Order_Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order_item = self.get_object(pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order_item = self.get_object(pk)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order_item = self.get_object(pk)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get all Order Items by Order id
class GetAllOrderItemsById(APIView):
    """
    List all Order Items.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        order = Order.objects.filter(pk=pk).first()
        order_item = Order_Item.objects.filter(order=order)
        serializer = OrderItemSerializer(order_item, many=True)
        return Response(serializer.data)
