from django.contrib import admin
from .models import Product
from .models import ProductInCart


admin.site.register(Product)
admin.site.register(ProductInCart)
