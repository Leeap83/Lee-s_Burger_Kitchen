from django.shortcuts import render
from products.models import Product, Ingredients


def about_us(request):
    """ A view to return about page """

    return render(request, 'customer/about.html')


def our_suppliers(request):
    """ A view to return about page """

    return render(request, 'customer/suppliers.html')


def place_order(request):
    """ A view to show all products """

    products = Product.objects.all()
    bites = Product.objects.filter(
        category__name__contains='bites')
    beef = Product.objects.filter(
        category__name__contains='beef_burgers')
    chicken = Product.objects.filter(
        category__name__contains='chicken_burgers')
    vegie = Product.objects.filter(
        category__name__contains='vegetarian_burgers')
    sides = Product.objects.filter(
        category__name__contains='fries_sides')
    sauces = Product.objects.filter(
        category__name__contains='sauces')

    context = {
        'products': products,
        'bites': bites,
        'beef': beef,
        'chicken': chicken,
        'vegie': vegie,
        'sides': sides,
        'sauces': sauces,
    }

    return render(request, 'customer/order.html', context)
