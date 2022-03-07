from django.db import models


class Product(models.Model):
    name = models.CharField( max_length=50)
    description =  models.TextField( max_length=150)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
# Create your models here.
