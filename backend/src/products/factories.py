"""Contains factories for product related models."""
from factory.django import DjangoModelFactory
from factory import Faker, sequence, lazy_attribute
from factory.fuzzy import FuzzyFloat
from random import choice

from .models import Category, Product


class CategoryFactory(DjangoModelFactory):
    """Product category Factory for Category model."""

    class Meta:
        model = Category

    @sequence
    def name(n):
        while True:
            fake = Faker("word")._get_faker()
            name = fake.word()
            try:
                _ = Category.objects.get(name=name)
                continue
            except Category.DoesNotExist:
                return name


class ProductFactory(DjangoModelFactory):
    """Product Factory for Product model."""

    class Meta:
        model = Product

    price = FuzzyFloat(low=0.0, high=1000.0)
    description = Faker("text")
    is_in_stock = Faker("pybool")

    @lazy_attribute
    def category(self):
        try:
            return choice([i for i in Category.objects.all()])
        except IndexError:
            return CategoryFactory.create()

    @sequence
    def name(n):
        while True:
            fake = Faker("word")._get_faker()
            name = fake.word()
            try:
                _ = Product.objects.get(name=name)
                continue
            except Product.DoesNotExist:
                return name
