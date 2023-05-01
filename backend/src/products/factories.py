"""Contains factories for product related models."""
from factory.django import DjangoModelFactory
from factory import Faker, sequence
from factory.fuzzy import FuzzyFloat
from random import choice

from .models import Category, Product


class CategoryFactory(DjangoModelFactory):
    """Product category Factory for Category model."""

    class Meta:
        model = Category

    name = Faker("word")


class ProductFactory(DjangoModelFactory):
    """Product Factory for Product model."""

    class Meta:
        model = Product

    name = Faker("word")
    price = FuzzyFloat(low=0.0, high=1000.0)
    description = Faker("text")
    is_in_stock = Faker("pybool")

    @sequence
    def category(_):
        try:
            return choice([i for i in Category.objects.all()])
        except IndexError:
            return CategoryFactory.create()
