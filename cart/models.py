import uuid
from django.db import models
from django.urls import reverse
from django.db.models import Sum
from django.conf import settings


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def category_url(self):
    #     return reverse('products_by_category', args=[self.slug])

    def get_absolute_url(self):
        return reverse(
         'products:categories_display',
         kwargs={'id': self.id, 'slug': self.slug}
    )

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def order_number(self):
    #     '''
    #     Generate a unique order number
    #     '''
    #     return uuid.uuid4().hex.upper()

    # def calculate_deliver(self):
    #     """
    #     Update order total depending on
    #     delivery
    #     """
    #     self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
    #     if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
    #         self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
    #     else:
    #         self.delivery_cost = 0
    #     self.grand_total = self.order_total + self.delivery_cost
    #     self.save()


    # def save(self, *args, **kwargs):
    #     '''
    #     If the order number hasn't been set already,
    #     override the original save method
    #     '''
    #     if not self.order_number:
    #         self.order_number = self.order_number()
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def category_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


# Cart Model
class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

        def __str__(self):
            return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product


# Order Model
class Order(models.Model):
    token = models.CharField(max_length=300, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Order Total')
    emailAddress = models.EmailField(
        max_length=300, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=300, blank=True)
    billingAddress = models.CharField(max_length=300, blank=True)
    billingCountry = models.CharField(max_length=300, blank=True)
    billingCity = models.CharField(max_length=300, blank=True)
    billingZip = models.CharField(max_length=300, blank=True)
    shippingName = models.CharField(max_length=300, blank=True)
    shippingAddress = models.CharField(max_length=300, blank=True)
    shippingCountry = models.CharField(max_length=300, blank=True)
    shippingCity = models.CharField(max_length=300, blank=True)
    shippingZip = models.CharField(max_length=300, blank=True)


class Meta:
    db_table = 'Order'
    ordering = ['-created']

    def __str__(self):
        return str(self.id)

    # def __str__(self):
    #     return self.order_number


class OrderItem(models.Model):
    product = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     '''
    #     Override the original save method to set the lineitem
    #     total and update the order total
    #     '''
    #     self.lineitem_total = self.product.price * self.quantity
    #     super().save(*args, **kwargs)

    class Meta:
        db_table = 'OrderItem'

    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product

    # def __str__(self):
    #     return f'SKU {self.product.sku} on order {self.order.order_number}'
