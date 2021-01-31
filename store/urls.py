from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products/', views.all_products, name='all_products'),
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.product, name='product_details'),
    path('account/create/', views.registrationView, name='register'),
    path('account/login/', views.loginView, name='login'),
    path('account/logout/', views.logoutView, name='logout'),
    path('history/', views.customerHistory, name='history'),
    path('search/', views.search, name='search'),
    path('order/<int:order_id>', views.viewOrder, name='view_order'),
]
