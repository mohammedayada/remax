from django.shortcuts import render
from .serializer import Brand, BrandSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

