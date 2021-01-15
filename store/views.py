from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'store/home_page.html', {
        'category': category_page, 'products': products})


def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'store/product.html', {'product': product})


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Please fill in your personal info'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress = request.POST['stripeBillingAddress']
            billingCountry = request.POST['stripeBillingCountry']
            billingCity = request.POST['stripeBillingCity']
            billingPostcode = request.POST['stripeBillingPostcode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress = request.POST['stripeShippingAddress']
            shippingCountry = request.POST['stripeShippingCountry']
            shippingCity = request.POST['stripeShippingCity']
            shippingPostcode = request.POST['stripeShippingPostcode']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='usd',
                description=description,
                customer=customer.id
            )

            try: 
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    billingName=billingName,
                    billingAddress=billingAddress,
                    billingCountry=billingCountry,
                    billingCity=billingCity,
                    billingPostcode=billingPostcode,
                    shippingName=shippingName,
                    shippingAddress=shippingAddress,
                    shippingCountry=shippingCountry,
                    shippingCity=shippingCity,
                    shippingPostcode=shippingPostcode
                )
                order_details.save()
                for order_item in cart_items:
                    or_item = OrderItem.objects.create(
                        product=order_item.product.name,
                        quantity=order_item.quantity,
                        price=order_item.product.price,
                        order=order_details
                    )
                    or_item.save()

                    #reducing the stock
                    products = 
        except stripe.error.CardError as e:
            return False, e

    return render(request, 'store/cart.html', dict(
        cart_items=cart_items, total=total,
        counter=counter, data_key=data_key,
        stripe_total=stripe_total, description=description))

