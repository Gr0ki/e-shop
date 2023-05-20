"""Contains models for orders app."""

from django.contrib.auth import get_user_model
from django.db import models

from ..products.models import Product


class Status(models.Model):
    """Status model."""

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    """Order model."""

    # pylint: disable=no-member
    customer = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(
        Status, default=None, null=True, on_delete=models.PROTECT
    )
    date_time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Customer name: {self.customer.username}. Status: {self.status.name}."


class OrderItem(models.Model):
    """OrderItem model."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order-id: {self.order.id}\nProduct: {self.product.name} Amount: {self.quantity}"
