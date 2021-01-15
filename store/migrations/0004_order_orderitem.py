# Generated by Django 3.1.4 on 2021-01-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=300)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=300, verbose_name='Email Address')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=300)),
                ('billingAddress', models.CharField(blank=True, max_length=300)),
                ('billingCountry', models.CharField(blank=True, max_length=300)),
                ('billingCity', models.CharField(blank=True, max_length=300)),
                ('billingPostcode', models.CharField(blank=True, max_length=300)),
                ('shippingName', models.CharField(blank=True, max_length=300)),
                ('shippingCounty', models.CharField(blank=True, max_length=300)),
                ('shippingCity', models.CharField(blank=True, max_length=300)),
                ('shippingPostcode', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
