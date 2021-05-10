from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Cart is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IaiTKDlSI8u0TYxOax3z1I3OfPJjohnXJ2vSLK6KWnQ7oojSVLHlgqZBhBDSO7BhgQxJ1XLU5EWy7QBS0GioH6a00pd7LbUzz',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
