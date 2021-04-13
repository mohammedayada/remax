from django.shortcuts import render
from .serializer import ItemSerializer, Item
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

