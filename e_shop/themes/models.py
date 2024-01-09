from django.db import models

# Create your models here.
class Theme(models.Model):
    banner = models.ImageField(upload_to='media/banners/')
    caption = models.TextField()