from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('category/<slug:category_slug>',
         views.home, name='products_by_category'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.product, name='product_details'),
    path('account/create/', views.registrationView, name='register'),
    path('account/login/', views.loginView, name='login'),
    path('account/logout/', views.logoutView, name='logout'),
    path('history/', views.customerHistory, name='history'),
    path('search/', views.search, name='search'),
    path('order_complete/<int:order_id>',
         views.completed_order, name='completed_order'),
]