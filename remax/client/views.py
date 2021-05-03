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
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SERVICE = 'smtp.gmail.com:587'
USERNAME = 'djangoproject95@gmail.com'
PASSWORD = 'hassan@1995'
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
        if 'email' in request.data:
            client = Client.objects.filter(email=request.data['email']).first()
            print(client)
            if client:

                clientSerializer = ClientSerializer(client)
                return Response(clientSerializer.data, status=status.HTTP_201_CREATED)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def send_email(fromaddr, toaddrs, number):
    # Create the plain-text and HTML version of your message
    message = f"""Subject: Your Key

    Hi, your key is {number}"""
    try:

        # connection = init_connection(SERVICE, USERNAME, PASSWORD)

        server = smtplib.SMTP(SERVICE)
        server.ehlo()
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.ehlo()
        server.sendmail(fromaddr, toaddrs, message.format(number=number))
        server.quit()
    except:
        logging.critical("cant start connection")

class ClientPostKey(APIView):
    """
    Create a new Key.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        if 'email' in request.data:
            number = random.randint(1000, 9999)
            client = Client.objects.filter(email=request.data['email']).first()
            if client:
                client.key = number
                client.save()
                send_email(USERNAME, client.email, number)
                clientSerializer = ClientSerializer(client)
                return Response(clientSerializer.data)
        return Response("You must send email", status=status.HTTP_400_BAD_REQUEST)

class ClientActiveKey(APIView):
    """
    Active Key.
    """
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        if 'email' in request.data and 'key' in request.data:
            client = Client.objects.filter(email=request.data['email']).first()
            if client:
                if client.key == int(request.data['key']):
                    client.is_active = True
                    client.save()
            clientSerializer = ClientSerializer(client)
            return Response(clientSerializer.data)
        return Response("You must send email and Key", status=status.HTTP_400_BAD_REQUEST)


# To Retrieve, update or delete a Client instance.
class ClientDetail(APIView):
    """
    Retrieve, update or delete a Client instance.
    """
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        client = Client.objects.filter(pk=pk).first()
        client_location = Client_Location.objects.filter(client=client)
        serializer = ClientLocationSerializer(client_location, many=True)
        return Response(serializer.data)
