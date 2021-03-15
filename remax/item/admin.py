from django.contrib import admin
from .models import Item, Item_Imgs
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Item_Imgs)
class Item_ImgsAdmin(admin.ModelAdmin):
    pass