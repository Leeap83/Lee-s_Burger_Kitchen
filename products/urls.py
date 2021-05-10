from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>/', views.product_details, name='product_details'),
    path(
        'custom_details/<product_id>/',
        views.custom_details, name='custom_details'),
]
