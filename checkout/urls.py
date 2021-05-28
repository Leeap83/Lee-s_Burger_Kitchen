from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_id>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('view_order/<str:pk>', views.view_order, name='view_order'),
]
