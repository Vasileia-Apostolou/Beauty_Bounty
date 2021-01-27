from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Product, Order
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from django.contrib.auth.models import Group, User
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages


def home(request):
    """
    This is view for the
    Homepage.
    """
    return render(request, 'store/home_page.html')


def all_products(request, category_slug=None):
    category_page = None
    products = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'store/all_products.html', {
        'category': category_page, 'products': products})


# PRODUCT
def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'store/product.html', {'product': product})


# REGISTRATION
def registrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            registration_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='Customer')
            user_group.user_set.add(registration_user)
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})


# LOGIN
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


# LOGOUT
def logoutView(request):
    logout(request)
    return redirect('login')


# ORDER HISTORY
@login_required(redirect_field_name='next', login_url='login')
def customerHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
    return render(request, 'store/history.html', {
        'order_details': order_details})


# SEARCH PRODUCT
def search(request):
    products = Product.objects.filter(name__contains=request.GET['product'])
    return render(request, 'store/all_products.html', {'products': products})
