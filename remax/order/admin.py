from django.contrib import admin
from .models import Order, Order_Item
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Order_Item)
class Order_Item_Admin(admin.ModelAdmin):
    pass