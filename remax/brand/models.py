from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='brands_imgs/', null=True)

    def __str__(self):
        return self.name