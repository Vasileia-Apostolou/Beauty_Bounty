from django.db import models
from django.urls import reverse
 

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


class OrderItem(models.Model):
    product = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def total(self):
        return self.quantity * self.price
    
    def __str__(self):
        return self.product


