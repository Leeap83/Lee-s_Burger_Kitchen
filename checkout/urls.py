from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_id>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view_order/<order_id>', views.view_order, name='view_order'),
    path('edit_status/<int:order_id>', views.edit_status, name='edit_status')
]
