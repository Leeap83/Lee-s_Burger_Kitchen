from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Ingredients

from .forms import CustomForm, ProductForm

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

    form = CustomForm()
    context = {
        'product': product,
        'ingredient': ingredient,
        'custom': custom,
        'form': form,
    }

    return render(request, 'products/custom_details.html', context)


def add_product(request):
    """Add a product to the database"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """Edit a product from the Menu"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """Delete a product from the Menu"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))
