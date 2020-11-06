from django.urls import path
from .import views

urlpatterns = [

    path('', views.products, name='home'),
    path('cart/', views.cart, name='cartpage'),
    path('checkout/', views.checkout, name='check'),
]