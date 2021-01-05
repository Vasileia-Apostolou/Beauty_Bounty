from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_details'),
    path('cart/add/<int_product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart'),
]