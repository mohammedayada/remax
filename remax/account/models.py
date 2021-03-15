from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    img = models.ImageField()


    def __str__(self):
        return self.client.name + " " + self.phone


