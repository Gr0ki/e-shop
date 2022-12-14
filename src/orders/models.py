from django.contrib.auth import get_user_model
from django.db import models

from ..products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    customer = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(
        Status, default=None, null=True, on_delete=models.PROTECT
    )  # TODO: Update default status
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
