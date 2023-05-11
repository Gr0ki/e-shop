"""Contains fixtures to test Django app."""

import pytest

from ....accounts.factories import UserFactory
from ....orders.factories import StatusFactory, OrderFactory, OrderItemFactory
from ....products.factories import CategoryFactory, ProductFactory


@pytest.fixture(scope="session")
def new_user():
    """Returns a link to a function that creates a User instance via UserFactory."""

    def _new_user(username: str = None):
        """
        Creates a User instance via UserFactory.
        username can be specified explicitly.
        """
        kwargs_keys = ("username",)
        kwargs_values = (username,)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return UserFactory(**kwargs)

    return _new_user


@pytest.fixture(scope="session")
def new_order_status():
    """Returns a link to a function that creates a Status instance via StatusFactory."""

    def _new_order_status(name: str = None):
        """
        Creates a Status instance via StatusFactory.
        Status name can be specified explicitly.
        """
        kwargs_keys = ("name",)
        kwargs_values = (name,)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return StatusFactory(**kwargs)

    return _new_order_status


@pytest.fixture(scope="session")
def new_order():
    """Returns a link to a function that creates a Order instance via OrderFactory."""

    def _new_order(customer=None, status=None):
        """
        Creates a Order instance via OrderFactory.
        Order customer and Order's status can be specified explicitly.
        """
        kwargs_keys = ("customer", "status")
        kwargs_values = (customer, status)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return OrderFactory(**kwargs)

    return _new_order


@pytest.fixture(scope="session")
def new_order_item():
    """Returns a link to a function that creates a OrderItem instance via OrderItemFactory."""

    def _new_order_item(order=None, product=None):
        """
        Creates a OrderItem instance via OrderItemFactory.
        OrderItem's Order and OrderItems's Product can be specified explicitly.
        """
        kwargs_keys = ("order", "product")
        kwargs_values = (order, product)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return OrderItemFactory(**kwargs)

    return _new_order_item


@pytest.fixture(scope="session")
def new_product_category():
    """Returns a link to a function that creates a Category instance via CategoryFactory."""

    def _new_product_category(name):
        """
        Creates a Category instance via CategoryFactory.
        Category name can be specified explicitly.
        """
        kwargs_keys = ("name",)
        kwargs_values = (name,)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return CategoryFactory(**kwargs)

    return _new_product_category


@pytest.fixture(scope="session")
def new_product():
    """Returns a link to a function that creates a Product instance via ProductFactory."""

    def _new_product(name=None, category=None, is_in_stock=None):
        """
        Creates a Product instance via ProductFactory.
        Product name, Category, and is_in_stock fields can be specified explicitly.
        """
        kwargs_keys = ("name", "category", "is_in_stock")
        kwargs_values = (name, category, is_in_stock)
        kwargs = {
            key: value
            for key, value in zip(kwargs_keys, kwargs_values)
            if value is not None
        }
        return ProductFactory(**kwargs)

    return _new_product
