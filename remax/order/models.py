from django.db import models
from django.utils.timezone import now
from client.models import Client,Client_Location
from item.models import Item

# Create your models here.
Status_Choices = [
    ('pre', 'Preparation'),
    ('del', 'Delivered'),
    ('not', 'Not delivered'),
]


class Order(models.Model):
    date_time = models.DateTimeField(default=now)
    status = models.CharField(choices=Status_Choices, max_length=3, default='pre')
    total = models.FloatField(default=0)
    delivery_cost = models.FloatField(default=0)
    address =models.ForeignKey(Client_Location, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + " " + str(self.total)


class Order_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('item', 'order',)

    def __str__(self):
        return str(self.order) + " " + str(self.item) + " quantity" + str(self.quantity)
