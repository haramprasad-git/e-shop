from django.contrib import admin
from . models import Product, Category, Size, ProductSize

# Register your models here.
admin.site.register([Product, Category, Size, ProductSize])