"""Tests for product related models."""

import pytest
from django.db import IntegrityError

from ...core.tests.shared.conftest import new_product_category, new_product


CATEGORY_NAME = "test_category"
PRODUCT_NAME = "test_product"
is_in_stock = True


@pytest.mark.django_db
def test_product_category_model_successful_creation(new_product_category):
    """Test successful creation of the Category model."""
    category = new_product_category(name=CATEGORY_NAME)
    assert isinstance(category.name, str)
    assert category.name == CATEGORY_NAME
    assert str(category.name) == CATEGORY_NAME


@pytest.mark.django_db
def test_product_category_model_unique_constrain_exception(new_product_category):
    """
    Test that an IntegrityError is raised when creating a new Category object
    with the same name as an existing one.
    """
    _ = new_product_category(name=CATEGORY_NAME)
    with pytest.raises(IntegrityError):
        _ = new_product_category(name=CATEGORY_NAME)


@pytest.mark.django_db
def test_order_model(new_product, new_product_category):
    """Test successful creation of the Product model."""

    category = new_product_category(name=CATEGORY_NAME)
    product = new_product(name=PRODUCT_NAME, category=category, is_in_stock=is_in_stock)
    assert isinstance(product.name, str)
    assert isinstance(product.price, float)
    assert isinstance(product.description, str)
    assert isinstance(product.is_in_stock, bool)
    assert product.name == PRODUCT_NAME
    assert product.category == category
    assert product.is_in_stock == is_in_stock
    assert (
        str(product)
        == f"Product name: {PRODUCT_NAME}. Price: {product.price}. Is in stock: {is_in_stock}."
    )
