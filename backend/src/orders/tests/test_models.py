"""Tests fot order related models."""

import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from ..models import Status, Order, OrderItem
from ...products.models import Product


STATUS_NAME = "test_status"
TEST_USERNAME = "test_user"
PRODUCT_NAME = "test_product"
ORDER_ITEM_QUANTITY = 135


@pytest.mark.django_db
def test_status_model_successful_creation():
    """Test successful creation of the Status model."""
    status = Status.objects.create(name=STATUS_NAME)
    assert status.name == STATUS_NAME
    assert str(status.name) == STATUS_NAME


@pytest.mark.django_db
def test_status_model_unique_constrain_exception():
    """
    Test that an IntegrityError is raised when creating a new Status object
    with the same name as an existing one.
    """
    _ = Status.objects.create(name=STATUS_NAME)
    with pytest.raises(IntegrityError):
        _ = Status.objects.create(name=STATUS_NAME)


@pytest.mark.django_db
def test_order_model():
    """Test successful creation of the Order model."""
    user = get_user_model().objects.create(username=TEST_USERNAME)
    status = Status.objects.create(name=STATUS_NAME)
    order = Order.objects.create(customer=user, status=status)
    assert order.customer.username == TEST_USERNAME
    assert order.status.name == STATUS_NAME
    assert (
        str(order)
        == f"Customer name: {order.customer.username}. Status: {order.status.name}."
    )


@pytest.mark.django_db
def test_order_item_model():
    """Test successful creation of the OrderItem model."""
    user = get_user_model().objects.create(username=TEST_USERNAME)
    status = Status.objects.create(name=STATUS_NAME)
    order = Order.objects.create(customer=user, status=status)
    product = Product.objects.create(name=PRODUCT_NAME, price=10.0)
    order_item = OrderItem.objects.create(
        order=order, product=product, quantity=ORDER_ITEM_QUANTITY
    )
    assert order_item.order == order
    assert order_item.product == product
    assert order_item.quantity == ORDER_ITEM_QUANTITY
    assert (
        str(order_item)
        == f"Order-id: {order.id}\nProduct: {product.name} Amount: {order_item.quantity}"
    )
