from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings


# CART
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# ADD TO CART
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


# PRODUCT
def product(request, category_slug, product_slug):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    if request.method == 'POST' and request.user.is_authenticated and request.POST['content'].strip() != '':
        Review.objects.create(product=product,
                              user=request.user,
                              content=request.POST['content'])
    reviews = Review.objects.filter(product=product)
    return render(request, 'store/product.html',
                  {'product': product, 'reviews': reviews})


# CART USER'S INFORMATION
def cart_detail(request, total=0, counter=0, cart_items=None, slug=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order_total = int(total * 100)
    description = 'Please Fill In Your Personal Info'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress = request.POST.get('stripeBillingAddress', False)
            billingCountry = request.POST.get('stripeBillingCounty', False)
            billingCity = request.POST.get('stripeBillingCity', False)
            billingZip = request.POST.get('stripeBillingZip', False)
            shippingName = request.POST['stripeShippingName']
            shippingAddress = request.POST.get('stripeShippingAddress', False)
            shippingCountry = request.POST.get('stripeShippingCountry', False)
            shippingCity = request.POST.get('stripeShippingAddressCity', False)
            shippingZip = request.POST.get('stripeShippingZip', False)
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=order_total,
                currency='usd',
                description=description,
                customer=customer.id
            )
            # Order
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    billingName=billingName,
                    billingAddress=billingAddress,
                    billingCountry=billingCountry,
                    billingCity=billingCity,
                    billingZip=billingZip,
                    shippingName=shippingName,
                    shippingAddress=shippingAddress,
                    shippingCountry=shippingCountry,
                    shippingCity=shippingCity,
                    shippingZip=shippingZip
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

                    # reducing the stock
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(
                        order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()

                    # print statement
                    print('Your order has been completed')
                return redirect('completed_order', order_details.id)
            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as e:
            return False, e

    return render(request, 'cart/cart.html', dict(
        cart_items=cart_items, total=total,
        counter=counter, data_key=data_key,
        order_total=order_total, description=description))


# COMPLETED ORDER PAGE
def completed_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/completed_order.html', {'order': order})


# DECEASE ITEM QUANTITY
def decrease_quantity(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    '''
      Checks if item quantity
      is greater than 1
    '''
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


# DELETE ITEM FROM CART
def remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')

