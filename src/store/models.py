from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    # image = models.ImageField()
    category = models.OneToOneField(
        Category, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    description = models.TextField(null=True, blank=True)
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f'Product name: {self.name}. Price: {self.price}. Is in stock: {self.is_in_stock}.'


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.CharField(max_length=200, default='created')
    date_time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Customer name: {self.customer}. Status: {self.status}.'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order}\n{self.product} Amount: {self.quantity}'
