from django.shortcuts import render
from .serializer import CategorySerializer, Category
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
class CategoryGetList(APIView):
    """
    List all Categories, or create a new Category.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryPostList(APIView):
    """
    List all categories, or create a new Category.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Category = self.get_object(pk)
        serializer = CategorySerializer(brand)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        Category = self.get_object(pk)
        serializer = CategorySerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)