from django.contrib import admin
from .models import Brand
# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass