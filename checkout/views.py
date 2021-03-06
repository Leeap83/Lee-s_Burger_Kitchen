from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.timezone import datetime
from django.db.models import Q

from .forms import OrderForm, StatusForm
from .models import Order, OrderLineItem
from products.models import Product, Custom_burger
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street': request.POST['street'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "A products in your cart wasn't found in the database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your Cart is Empty")
            return redirect(reverse('products'))

        current_bag = cart_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    # 'full_name': profile.user.get.full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street': profile.default_street,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is Missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_id):
    """Handle successful checkouts"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street': order.street,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_id}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@login_required
def dashboard(request):
    """ A view to return todays orders"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

    today = datetime.today()
    orders = Order.objects.filter(
        created_on__year=today.year,
        created_on__month=today.month,
        created_on__day=today.day
    )

    total_revenue = 0
    for order in orders:
        total_revenue += order.order_total

    context = {
        'orders': orders,
        'total_revenue': total_revenue,
        'total_orders': len(orders)
    }

    return render(request, 'checkout/dashboard.html', context)


@login_required
def all_orders(request):
    """ A view to return all orders"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

    orders = Order.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "No Orders found")
                return redirect(reverse('all_orders'))

            queries = (
                Q(name__icontains=query)
                | Q(email__icontains=query)
                | Q(id__icontains=query)
                | Q(order_status__icontains=query)
                | Q(created_on__icontains=query)
            )
            orders = orders.filter(queries)

    context = {
        'orders': orders,
        'search_term': query,
    }

    return render(request, 'checkout/all_orders.html', context)


@login_required
def view_order(request, pk):
    """View Order details and update status"""
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied')
        return redirect(reverse('home'))

    custom = Custom_burger.objects.all()
    order = Order.objects.get(id=pk)
    product = Product.objects.all()
    form = StatusForm(instance=order)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    template = 'checkout/view_order.html'
    context = {
        'order': order,
        'form': form,
        'product': product,
        'custom': custom,

    }

    return render(request, template, context)
