"""Contains factories for order related models."""
from factory.django import DjangoModelFactory
from factory import Faker, sequence
from random import choice
from datetime import datetime

from ..accounts.factories import UserFactory
from django.contrib.auth import get_user_model
from .models import Status, Order, OrderItem
from ..products.models import Product
from ..products.factories import ProductFactory


class StatusFactory(DjangoModelFactory):
    """Order status Factory for Status model."""

    class Meta:
        model = Status

    @sequence
    def name(n):
        while True:
            name = Faker("word")
            try:
                _ = Status.objects.get(name=name)
                continue
            except Status.DoesNotExist:
                return name


class OrderFactory(DjangoModelFactory):
    """Order Factory for Order model."""

    class Meta:
        model = Order

    date_time_updated = Faker(
        "date_between_dates",
        date_start=datetime(2000, 1, 1),
        date_end=datetime(2022, 1, 1),
    )

    @sequence
    def customer(n):
        try:
            return choice([i for i in get_user_model().objects.all()])
        except IndexError:
            return UserFactory.create()

    @sequence
    def status(n):
        try:
            return choice([i for i in Status.objects.all()])
        except IndexError:
            return StatusFactory.create()


class OrderItemFactory(DjangoModelFactory):
    """OrderItem Factory for OrderItem model."""

    class Meta:
        model = OrderItem

    quantity = Faker("random_int")
    date_time_added = Faker(
        "date_between_dates",
        date_start=datetime(2000, 1, 1),
        date_end=datetime(2022, 1, 1),
    )

    @sequence
    def order(_n):
        try:
            return choice([i for i in Order.objects.all()])
        except IndexError:
            return OrderFactory.create()

    @sequence
    def product(n):
        try:
            return choice([i for i in Product.objects.all()])
        except IndexError:
            return ProductFactory.create()
