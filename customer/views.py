from django.shortcuts import render


def about_us(request):
    """ A view to return about page """

    return render(request, 'customer/about.html')


def our_suppliers(request):
    """ A view to return about page """

    return render(request, 'customer/suppliers.html')
