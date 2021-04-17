from django.shortcuts import render
from .serializer import (
    Client_Phone,
    Client,
    Client_Location,
    ClientSerializer,
    ClientPhoneSerializer,
    ClientLocationSerializer
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ClientPhoneViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientPhoneSerializer
    queryset = Client_Phone.objects.all()

class ClientLocationViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientLocationSerializer
    queryset = Client_Location.objects.all()
