from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name + " " + self.email


class Client_Phone(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.client.name + " " + self.phone


class Client_Location(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.client.name + " " + self.location


