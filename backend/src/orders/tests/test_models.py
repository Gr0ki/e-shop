"""Tests fot order related models."""

import pytest
from datetime import datetime
from django.db import IntegrityError

from ...core.tests.shared.conftest import (
    new_order_status,
    new_order,
    new_order_item,
    new_user,
    new_product,
)
from .shared import STATUS_NAME, TEST_USERNAME, PRODUCT_NAME


@pytest.mark.django_db
def test_status_model_successful_creation(new_order_status):
    """Test successful creation of the Status model."""
    status = new_order_status(name=STATUS_NAME)
    assert isinstance(status.name, str)
    assert status.name == STATUS_NAME
    assert str(status.name) == STATUS_NAME


@pytest.mark.django_db
def test_status_model_unique_constrain_exception(new_order_status):
    """
    Test that an IntegrityError is raised when creating a new Status object
    with the same name as an existing one.
    """
    status = new_order_status(name=STATUS_NAME)
    with pytest.raises(IntegrityError):
        status = new_order_status(name=STATUS_NAME)


@pytest.mark.django_db
def test_order_model(new_user, new_order_status, new_order):
    """Test successful creation of the Order model."""
    user = new_user(username=TEST_USERNAME)
    status = new_order_status(name=STATUS_NAME)
    order = new_order(customer=user, status=status)
    assert order.customer == user
    assert order.status == status
    assert isinstance(order.date_time_updated, datetime)
    assert str(order) == f"Customer name: {TEST_USERNAME}. Status: {STATUS_NAME}."


@pytest.mark.django_db
def test_order_item_model(new_product, new_order, new_order_item):
    """Test successful creation of the OrderItem model."""
    order = new_order()
    product = new_product(name=PRODUCT_NAME)
    order_item = new_order_item(order=order, product=product)
    assert order_item.order == order
    assert order_item.product == product
    assert isinstance(order_item.quantity, int)
    assert isinstance(order_item.date_time_added, datetime)
    assert (
        str(order_item)
        == f"Order-id: {order.id}\nProduct: {PRODUCT_NAME} Amount: {order_item.quantity}"
    )
