
from re import template
from tkinter import Entry
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product

def product_list(request):
    return render( request, 'products/product_list.html' , {})

class ProductListView(ListView): 
    model = Product
    template_name = 'products/product_list.html'

class ProductInCartListView(ListView): 
    def get_queryset(self):
        Entry.objects.filter(user=self.request.user)
class ProductDetailView(DetailView): 
    model = Product
    template_name = 'products/product_detail.html'

    # Create your view here.
