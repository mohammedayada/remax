from rest_framework import serializers
from .models import Client, Client_Phone, Client_Location
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ClientPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Phone
        fields = "__all__"

class ClientLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Location
        fields = "__all__"

