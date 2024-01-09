from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
class Cart(models.Model):
    PRE_ORDER = 0
    CART_STAGES = (
        ('Order Approved', 1),
        ('Order Delivered', 2),
        ('Order Rejected', -1),
        ('Order Cancelled', -2)
    )

    owner = models.OneToOneField(Customer, related_name='customer', on_delete=models.CASCADE)
    cart_status = models.IntegerField(choices=CART_STAGES, default=PRE_ORDER)
    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, related_name='cart_item')
    quantity = models.PositiveSmallIntegerField()
