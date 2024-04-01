from typing import Any
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Size(models.Model):
    size = models.CharField()

    def __str__(self) -> str:
        return self.size
    

class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/Categry')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    DELETE_CHOICES = ((1, 'Live'), (0, 'Delete'))
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Products')
    mrp = models.FloatField()
    discount_percent = models.FloatField(validators=[MaxValueValidator(100)])
    available_sizes = models.ManyToManyField(Size, through='ProductSize')
    last_modification_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET('Others'))
    priority = models.IntegerField()
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=1)

    def __str__(self) -> str:
        return self.title

    def __add__(self, other) -> int:
        self_price = self.mrp * ((100-self.discount_percent) / 100)
        other_price = other.mrp * ((100-other.discount_percent) / 100)
        return self_price + other_price
    
class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='avilable_sizes', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, related_name='available_products', on_delete=models.CASCADE)
    stock = models.IntegerField()
    age_limit = models.CharField(blank=True, default='Not Given !')

    def __str__(self) -> str:
        return str(self.size) + ' ' + str(self.product)
