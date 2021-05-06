from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('our_suppliers/', views.our_suppliers, name='our_suppliers'),
    path('place_order/', views.place_order, name='place_order'),
]
