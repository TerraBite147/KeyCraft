from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Manufacturer
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    manufacturers = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == "manufacturer":
                sortkey = "manufacturer__name"
            elif sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "manufacturer" in request.GET:
            manufacturers = request.GET["manufacturer"].split(",")
            if manufacturers:
                manufacturer_q_objects = Q()
                for manufacturer in manufacturers:
                    manufacturer_q_objects |= Q(name__iexact=manufacturer)

                manufacturers_qs = Manufacturer.objects.filter(manufacturer_q_objects)
                products = products.filter(manufacturer__in=manufacturers_qs)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search query")
                return redirect(reverse("products"))

            # Regex pattern for whole word matching
            regex_pattern = r"\b" + query + r"\b"
            queries = Q(name__iregex=regex_pattern) | Q(
                description__iregex=regex_pattern
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_manufacturers": (
            manufacturers_qs if "manufacturer" in request.GET else None
        ),
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to render product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


def add_product(request):
    """Add a product to the store"""
    form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)