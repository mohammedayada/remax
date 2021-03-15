from django.db import models
from django.conf import settings
from category.models import Category
from brand.models import Brand
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    details = models.TextField()
    quantity = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.quantity


class Item_Imgs(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    img = models.ImageField()


    def __str__(self):
        return self.item.name