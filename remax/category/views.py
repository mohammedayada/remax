from django.shortcuts import render
from .serializer import CategorySerializer, Category
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

