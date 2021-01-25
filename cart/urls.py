from django.urls import path
from .views import (add_cart, cart_detail)

urlpatterns = [
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart', cart_detail, name='cart_detail'),
]