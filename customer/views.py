from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from customer.models import Review

from customer.forms import RatingForm


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


def reviews(request):
    """ A view to display all reviews """
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'customer/reviews.html', context)


@login_required
def add_review(request):
    """ A view to add a review """
    user = request.user
    form = RatingForm()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.save()
            messages.success(request, 'Successfully added a review!')
            return redirect('reviews')

    template = 'customer/add_review.html'

    context = {
        'form': form,
        'user': user,
    }

    return render(request, template, context)
