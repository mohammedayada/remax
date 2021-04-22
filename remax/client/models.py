from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name + " " + self.email


class Client_Phone(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    class Meta:
        unique_together = ('client', 'phone',)


    def __str__(self):
        return self.client.name + " " + self.phone


class Client_Location(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.CharField(max_length=10)
    class Meta:
        unique_together = ('client', 'location',)


    def __str__(self):
        return self.client.name + " " + self.location


