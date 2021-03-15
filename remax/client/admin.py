from django.contrib import admin
from .models import Client, Client_Phone, Client_Location
# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Client_Location)
class Client_LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Client_Phone)
class Client_phoneAdmin(admin.ModelAdmin):
    pass