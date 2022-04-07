from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from products.models import Product, ProductInCart
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductInCartListView(ListView):
    template_name = 'products/cart.html'

    def get_queryset(self):
        ProductInCart.objects.filter(user=self.request.user)


@method_decorator(login_required, name='get')
class ProductInCartCreateView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['product_id'])
        is_in_cart = ProductInCart.objects.filter(product=product).exists()
        if is_in_cart:
            product_in_cart = ProductInCart.objects.get(product=product)
            product_in_cart.amount += 1
            product_in_cart.save()
        else:
            product_in_cart = ProductInCart()
            product_in_cart.customer = request.user
            product_in_cart.product = product
            product_in_cart.amount = 1
            product_in_cart.save()
        return redirect('/cart')


@method_decorator(login_required, name='get')
class ProductInCartDeleteView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['product_id'])
        product_in_cart = ProductInCart.objects.get(product=product)
        if product_in_cart.amount > 1:
            product_in_cart.amount -= 1
            product_in_cart.save()
        else:
            product_in_cart.delete()
        return redirect('/cart')
