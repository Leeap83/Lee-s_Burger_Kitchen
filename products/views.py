from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Ingredients

from .forms import CustomForm

# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    categories = None
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def custom_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    ingredient = Ingredients.objects.all()
    custom = Product.objects.filter(
        category__name__contains='custom_burgers')

    custom_form = CustomForm()
    context = {
        'product': product,
        'ingredient': ingredient,
        'custom': custom,
        'custom_form': custom_form,
    }

    return render(request, 'products/custom_details.html', context)
