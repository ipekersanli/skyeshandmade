from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from products.models import Product, ProductInCart
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductInCartListView(ListView):
    template_name = 'products/products_in_cart.html'

    def get_queryset(self):
        ProductInCart.objects.filter(user=self.request.user)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


@method_decorator(login_required, name='get')
class ProductInCartCreateView(View):
    def get(self, request, *args, **kwargs):
        # product in cart yarat, customer olarak request.user kullanabilirsin
        # url lere ekledim, add-to-cart/5 e erisilirse id'si 5 olan product, product in cart objesinin,
        # product'u olacak, yazdigin modelleri unutma bol bol googlla,
        # bu sayiya kwargs['product_id'] ile erisebilirsin.
        return redirect('/') # bu da operasyon bitince redirectliyor, tirnak icindeki urlye
