from django.views.generic import ListView, DetailView
from products.models import Product, ProductInCart


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductInCartListView(ListView):
    def get_queryset(self):
        ProductInCart.objects.filter(user=self.request.user)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
