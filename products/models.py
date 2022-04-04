from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.name


class ProductInCart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.OneToOneField("products.Product", on_delete=models.CASCADE)
    amount = models.IntegerField()
