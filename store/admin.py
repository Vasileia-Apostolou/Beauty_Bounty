from django.contrib import admin
from cart.models import Product, Category, Order, OrderItem, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 15


admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False

    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = ['id', 'billingName', 'emailAddress', 'created']
        list_display_links = ('id', 'billingName')
        search_fields = ['id', 'billingName', 'emailAddress']
        readonly_fields = [
            'id', 'token', 'total', 'emailAddress', 'created', 'billingName',
            'billingAddress',  'billingCountry', 'billingCity', 'billingZip',
            'shippingName', 'shippingAddress', 'shippingCountry',
            'shippingCity', 'shippingZip']

        fieldsets = [
            ('ORDER INFORMATION', {'fields':
             ['id', 'token', 'total', 'created']}),
            ('BILLING INFORMATION', {'fields':
             ['emailAddress', 'billingName', 'billingAddress',
              'billingCountry', 'billingCity', 'billingZip']}),
            ('SHIPPING INFORMATION', {'fields':
             ['shippingName', 'shippingAddress',
              'shippingCountry', 'shippingCity', 'shippingZip']}),
        ]

        def has_delete_permission(self, request, obj=None):
            return False


admin.site.register(Review)

