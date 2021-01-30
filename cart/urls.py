from django.urls import path, include
from .views import (add_cart, cart_detail, completed_order,
                    decrease_quantity, remove_product)


urlpatterns = [
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart', cart_detail, name='cart_detail'),
    path('order_complete/<int:order_id>',
         completed_order, name='completed_order'),
    path('decrease/quantity/<int:product_id>',
         decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:product_id>',
         remove_product, name='remove_product'),
]