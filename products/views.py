from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Manufacturer

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    manufacturer = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'manufacturer' in request.GET:
            manufacturer = request.GET['manufacturer']
            if manufacturer:
                products = products.filter(manufacturer__name__iexact=manufacturer)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search query")
                return redirect(reverse('products'))

            # Regex pattern for whole word matching
            regex_pattern = r'\b' + query + r'\b'
            queries = Q(name__iregex=regex_pattern) | Q(description__iregex=regex_pattern)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_manufacturer': manufacturer,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to render product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
