from django.contrib.auth.models import User
from django.db import models

from ..products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"Status: {self.name}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    date_time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Customer name: {self.customer}. Status: {self.status}."


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.order}\nProduct: {self.product} Amount: {self.quantity}"
