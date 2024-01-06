from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    DELETE_CHOICES = ((1, 'Live'), (0, 'Delete'))

    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    mrp = models.FloatField()
    discount_percent = models.FloatField(validators=[MaxValueValidator(100)])
    last_modification_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, default=Category(name='Others'), on_delete=models.SET_DEFAULT)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=1)

    def __str__(self) -> str:
        return self.title