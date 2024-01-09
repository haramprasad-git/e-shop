from django.db import models
from django.contrib.auth.models import User

# District list for address
DISTRICT_LIST = (
        ('Thiruvananthapuram', 'Thiruvananthapuram'),
        ('Kollam', 'Kollam'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Alappuzha', 'Alappuzha'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'),
        ('Thrissur', 'Thrissur'),
        ('Palakkad', 'Palakkad'),
        ('Malappuram', 'Malappuram'),
        ('Kozhikkode', 'Kozhikkode'),
        ('Wayanad', 'Wayanad'),
        ('Kannur', 'Kannur'),
        ('Kasargode', 'Kasargode')
    )


class Customer(models.Model):
    core_user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, help_text='Use an Indian phone number without country code')
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.core_user.username


# Data Model to store Customer Address.
class Address(models.Model):
    district = models.CharField(choice=DISTRICT_LIST, required=True)
    city = models.CharField(max_length=500, required=True)
    street = models.CharField(max_length=500)
    building_no = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, related_name='address', on_delete=models.CASCADE)

    def __str__(self) -> str:
        if self.street:
            return '{}, {}'.format(self.street, self.city)
        else:
            return '{}, {}'.format(self.city, self.district)