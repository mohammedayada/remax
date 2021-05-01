from django.shortcuts import render
from .serializer import ItemSerializer, Item, Item_Imgs, ItemImgSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from category.models import Category
from brand.models import Brand
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

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


class GetItemDetail(APIView):
    """
    Retrieve Item instance.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


# Retrieve, update or delete a Item instance
class UpdateOrDeleteItemDetail(APIView):
    """
    update or delete a Item instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

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


class DeleteItemImg(APIView):
    """
    Delete a Item instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Item_Imgs.objects.get(pk=pk)
        except Item_Imgs.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        item_img = self.get_object(pk)
        item_img.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get items by category id
class ItemGetListByCategoryId(APIView):
    """
    List Items by category id.
    """
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        category = Category.objects.filter(pk=pk).first()
        items = Item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# To get items by brand id
class ItemGetListByBrandId(APIView):
    """
    List Items by Brand id.
    """
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        brand = Brand.objects.filter(pk=pk).first()
        items = Item.objects.filter(brand=brand)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


# To search by using name
class ItemSearchView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'details']
    filterset_fields = ['name', 'details']

