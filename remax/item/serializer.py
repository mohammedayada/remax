from rest_framework import serializers
from .models import Item, Item_Imgs
class ItemSerializer(serializers.ModelSerializer):
    # Create a custom method field
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Item
        fields = ['id', 'user', 'name', 'price', 'details', 'quantity', 'discount', 'category', 'brand']




class ItemImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Imgs
        fields = "__all__"

