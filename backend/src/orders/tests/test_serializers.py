"""Contains tests for order related serializers."""

import pytest
from pytest import approx
from random import randint
from datetime import datetime

from ...core.tests.shared.conftest import (
    new_order_status,
    new_order,
    new_order_item,
    new_user,
    new_product,
)
from ..serializers import StatusSerializer, OrderSerializer, OrderItemSerializer
from .shared import fake, convert_datetime_to_str_timestamp


@pytest.mark.django_db
def test_serialization_order_status_serializer(new_order_status):
    """Tests successful serialization with StatusSerializer."""
    status = new_order_status()
    serializer = StatusSerializer(status)
    assert serializer.data == {"id": status.id, "name": status.name}


@pytest.mark.django_db
def test_deserialization_order_status_serializer():
    """Tests successful deserialization with StatusSerializer."""
    data = {
        "name": fake.word(),
    }
    serializer = StatusSerializer(data=data)
    assert serializer.is_valid()
    status = serializer.save()
    assert status.name == data["name"]


@pytest.mark.django_db
def test_serialization_order_serializer(new_order):
    """Tests successful serialization with OrderSerializer."""
    order = new_order()
    serializer = OrderSerializer(order)
    assert serializer.data == {
        "id": order.id,
        "customer": order.customer.id,
        "status": order.status.id,
        "date_time_updated": convert_datetime_to_str_timestamp(order.date_time_updated),
    }


@pytest.mark.django_db
def test_deserialization_order_serializer(new_user, new_order_status):
    """Tests successful deserialization with OrderSerializer."""
    user = new_user()
    status = new_order_status()
    data = {
        "customer": user.id,
        "status": status.id,
        "date_time_updated": datetime.now(),
    }
    serializer = OrderSerializer(data=data)
    assert serializer.is_valid()
    order = serializer.save()
    assert order.customer == user
    assert order.status == status
    assert order.date_time_updated.timestamp() == approx(
        data["date_time_updated"].timestamp(), abs=0.01
    )


@pytest.mark.django_db
def test_serialization_order_item_serializer(new_order_item):
    """Tests successful serialization with OrderItemSerializer."""
    order_item = new_order_item()
    serializer = OrderItemSerializer(order_item)
    assert serializer.data == {
        "id": order_item.id,
        "quantity": order_item.quantity,
        "date_time_added": convert_datetime_to_str_timestamp(
            order_item.date_time_added
        ),
        "order": order_item.order.id,
        "product": order_item.product.id,
    }


@pytest.mark.django_db
def test_deserialization_order_item_serializer(new_order, new_product):
    """Tests successful deserialization with OrderItemSerializer."""
    order = new_order()
    product = new_product()
    data = {
        "quantity": randint(1, 200),
        "date_time_added": datetime.now(),
        "order": order.id,
        "product": product.id,
    }
    serializer = OrderItemSerializer(data=data)
    assert serializer.is_valid()
    order_item = serializer.save()
    assert order_item.quantity == data["quantity"]
    assert order_item.date_time_added.timestamp() == approx(
        data["date_time_added"].timestamp(), abs=0.01
    )
    assert order_item.order == order
    assert order_item.product == product
