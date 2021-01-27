from django.urls import path
from .views import (add_cart, cart_detail, completed_order, remove_product)


urlpatterns = [
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart', cart_detail, name='cart_detail'),
    path('order_complete/<int:order_id>',
         completed_order, name='completed_order'),
    path('product/remove/<int:product_id>',
         remove_product, name='remove_product'),
]