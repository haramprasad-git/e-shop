# Generated by Django 5.0.1 on 2024-01-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_priority_product_special_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='special_category',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'New Arrival'), (2, 'Great Discount'), (3, 'Featured Product')], default=0),
        ),
    ]
