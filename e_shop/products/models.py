from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    DELETE_CHOICES = ((1, 'Live'), (0, 'Delete'))
    SPECIAL_CATEGORY_CHOICES = ((0, 'None'), (1, 'New Arrival'), (2, 'Great Discount'), (3, 'Featured Product'))

    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    mrp = models.FloatField()
    discount_percent = models.FloatField(validators=[MaxValueValidator(100)])
    last_modification_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET('Others'))
    priority = models.IntegerField()
    special_category = models.IntegerField(choices=SPECIAL_CATEGORY_CHOICES, default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=1)

    def __str__(self) -> str:
        return self.title

    def __add__(self, other) -> int:
        self_price = self.mrp * ((100-self.discount_percent) / 100)
        other_price = other.mrp * ((100-other.discount_percent) / 100)
        return self_price + other_price