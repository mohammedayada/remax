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
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# To get all Clients
class ClientGetList(APIView):
    """
    List all Clients.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


# To post Clients
class ClientPostList(APIView):
    """
    Create a new Client.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if 'email' in request.data:
            client = Client.objects.filter(email=request.data['email']).first()
            if client:
                clientSerializer = ClientSerializer(client)
                return Response(clientSerializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Client instance.
class ClientDetail(APIView):
    """
    Retrieve, update or delete a Client instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get all Client phone
class ClientPhoneGetList(APIView):
    """
    List all Client Phone.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        client_phone = Client_Phone.objects.all()
        serializer = ClientPhoneSerializer(client_phone, many=True)
        return Response(serializer.data)


# To post Client Phone
class ClientPhonePostList(APIView):
    """
    Create a new Client Phone.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ClientPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Client Phone instance.
class ClientPhoneDetail(APIView):
    """
    Retrieve, update or delete a Client Phone instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Client_Phone.objects.get(pk=pk)
        except Client_Phone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client_phone = self.get_object(pk)
        serializer = ClientPhoneSerializer(client_phone)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client_phone = self.get_object(pk)
        serializer = ClientPhoneSerializer(client_phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client_phone = self.get_object(pk)
        client_phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get all Client phone by client id
class GetAllClientPhonesById(APIView):
    """
    List all Client Phone.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        client = Client.objects.filter(pk=pk).first()
        client_phone = Client_Phone.objects.filter(client=client)
        serializer = ClientPhoneSerializer(client_phone, many=True)
        return Response(serializer.data)


# To get all Client Location
class ClientLocationGetList(APIView):
    """
    List all Client Location.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        client_location = Client_Location.objects.all()
        serializer = ClientLocationSerializer(client_location, many=True)
        return Response(serializer.data)


# To post Client Location
class ClientLocationPostList(APIView):
    """
    Create a new Client Location.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ClientLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Client Location instance.
class ClientLocationDetail(APIView):
    """
    Retrieve, update or delete a Client Location instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Client_Location.objects.get(pk=pk)
        except Client_Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client_location = self.get_object(pk)
        serializer = ClientLocationSerializer(client_location)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client_location = self.get_object(pk)
        serializer = ClientLocationSerializer(client_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client_location = self.get_object(pk)
        client_location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# To get all Client Location by client id
class GetAllClientLocationsById(APIView):
    """
    List all Client Location.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        client = Client.objects.filter(pk=pk).first()
        client_location = Client_Location.objects.filter(client=client)
        serializer = ClientLocationSerializer(client_location, many=True)
        return Response(serializer.data)
