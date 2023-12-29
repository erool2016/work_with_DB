from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from main1.models import Product, Category


def product_list(request):
    #?price_from=10000&price_to=50000 -> {'price_from': '10000', 'price_to': '50000'}
    product = Product.objects.all()
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    if price_from:
        product = product.filter(price__gte=price_from)

    if price_to:
        product = product.filter(price__lte=price_to)
    search_query = request.GET.get('search')
    if search_query:
        product = product.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    template_name = 'list.html'
    return render(request, template_name,{'product': product})

def product_by_category(request, category_id):
    category = get_object_or_404(Category, slug=category_id)
    product = category.products.all()
    template = 'list.html'
    return render(request, template, {'product': product})


