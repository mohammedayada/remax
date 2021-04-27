from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(User):
    phone = models.CharField(max_length=11)
    img = models.ImageField(upload_to='accounts_imgs/', null=True)

    def __str__(self):
        return self.username + " " + self.phone


