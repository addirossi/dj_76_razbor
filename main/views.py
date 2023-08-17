from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from main.models import Product


# Create your views here.
def products_list_view(request):
    template_name = 'main/list.html'
    products = Product.objects.all()
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 0)
    if price_from:
        products = products.filter(price__gte=price_from)
    if price_to:
        products = products.filter(price__lte=price_to)
    return render(request, template_name, context={'products': products})


class ProductListView(View):
    def get(self, request):
        template_name = 'main/list.html'
        products = Product.objects.all()
        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 0)
        if price_from:
            products = products.filter(price__gte=price_from)
        if price_to:
            products = products.filter(price__lte=price_to)
        return render(request, template_name, context={'products': products})


def products_by_category(request, category_id):
    template_name = 'main/list.html'
    products = Product.objects.filter(category__slug=category_id)
    return render(request, template_name, context={'products': products})


class ProductsByCategory(ListView):
    queryset = Product.objects.all()
    template_name = 'main/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category__slug=category_id)
