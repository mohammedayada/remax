from django.shortcuts import render
from .serializer import ItemSerializer, Item, Item_Imgs, ItemImgSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# To get all items
class ItemGetList(APIView):
    """
    List all Items, or create a new Item.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# To post new Item
class ItemPostList(APIView):
    """
    List all Items, or create a new Item.
    """
    permission_classes = [IsAuthenticated]


    def get_object(self, requset):
        try:
            return requset.user
        except Item.DoesNotExist:
            raise Http404



    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data['user'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update or delete a Item instance
class ItemDetail(APIView):
    """
    Retrieve, update or delete a Item instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# To get all images
class ItemImgGetList(APIView):
    """
    List all Item imgs, or create a new Item.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        item_img = Item_Imgs.objects.all()
        serializer = ItemImgSerializer(item_img, many=True)
        return Response(serializer.data)

# To post one image to one item
class ItemImgPostList(APIView):
    """
    List all Items imgs, or create a new Item.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ItemImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To get all images for one item
class ItemImgForItem(APIView):
    """
    Retrieve, update or delete a Item instance.
    """
    permission_classes = [AllowAny]

    def get_object(self, item):
        try:
            return Item_Imgs.objects.filter(item=item)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = Item.objects.filter(pk=pk).first()
        item_img = self.get_object(item)
        serializer = ItemImgSerializer(item_img, many=True)
        return Response(serializer.data)


