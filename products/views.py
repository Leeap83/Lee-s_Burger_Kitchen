from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Custom_burger, Ingredients

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


@login_required
def add_product(request):
    """Add a product to the database"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

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


@login_required
def edit_product(request, product_id):
    """Edit a product from the Menu"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, product_id):
    """Delete a product from the Menu"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))


def custom(request):
    """ A view to display all custom_burgers """
    burgers = Custom_burger.objects.all()
    products = Product.objects.all()

    template = 'products/custom.html'

    context = {
        'burgers': burgers,
        'products': products,
    }

    return render(request, template, context)


@login_required
def custom_details(request, product_id):
    """ A view to add custom burger product details """
    product = get_object_or_404(Product, pk=product_id)
    ingredients = Ingredients.objects.all()
    form = CustomForm()

    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created Burger!')
    else:
        form = CustomForm()

    template = 'products/custom_details.html'

    context = {
        'product': product,
        'form': form,
        'ingredients': ingredients,

    }

    return render(request, template, context)
