"""Contains tests for product related serializers."""

import pytest

from ...core.tests.shared.conftest import new_product_category, new_product
from ..serializers import CategorySerializer, ProductSerializer


@pytest.mark.django_db
def test_serialization_category_serializer(new_product_category):
    """Tests successful serialization with CategorySerializer."""
    category = new_product_category()
    serializer = CategorySerializer(category)
    assert serializer.data == {"id": category.id, "name": category.name}


@pytest.mark.django_db
def test_deserialization_category_serializer():
    """Tests successful deserialization with CategorySerializer."""
    data = {
        "name": "test_category",
    }
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()
    category = serializer.save()
    assert category.name == data["name"]


@pytest.mark.django_db
def test_serialization_product_serializer(new_product_category, new_product):
    """Tests successful serialization with ProductSerializer."""
    category = new_product_category()
    product = new_product()
    serializer = ProductSerializer(product)
    assert serializer.data == {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "category": category.id,
        "description": product.description,
        "is_in_stock": product.is_in_stock,
    }


@pytest.mark.django_db
def test_deserialization_product_serializer(new_product_category):
    """Tests successful deserialization with ProductSerializer."""
    category = new_product_category()
    data = {
        "name": "test_product",
        "price": 10.0,
        "category": category.id,
        "description": "test_description",
        "is_in_stock": True,
    }
    serializer = ProductSerializer(data=data)
    assert serializer.is_valid()
    product = serializer.save()
    assert product.name == data["name"]
    assert product.price == data["price"]
    assert product.category == category
    assert product.description == data["description"]
    assert product.is_in_stock == data["is_in_stock"]
