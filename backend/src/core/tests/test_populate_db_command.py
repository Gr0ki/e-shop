"""
Test with unittest approach custom Django management command for populating db.
"""
from unittest.mock import patch
from io import StringIO
import pytest

from django.core.management import call_command
from django.test import TestCase

from django.contrib.auth import get_user_model
from ...orders.models import Status, Order, OrderItem
from ...products.models import Category, Product


@patch("src.core.management.commands.populate_db.Command.check")
@pytest.mark.django_db
class CommandTests(TestCase):
    """Tests for django CLI command."""

    def test_populate_db_ready(self, patched_check):
        """Tests if database populated correctly."""
        patched_check.return_value = True

        users = get_user_model().objects.all()
        statuses = Status.objects.all()
        orders = Order.objects.all()
        order_items = OrderItem.objects.all()
        categories = Category.objects.all()
        products = Product.objects.all()

        out = StringIO()
        call_command("populate_db", stdout=out)

        assert out.getvalue() == "Database was successfuly populated!\n"
        assert len(users) == 5
        assert len(statuses) == 3
        assert len(orders) == 40
        assert len(order_items) == 60
        assert len(categories) == 4
        assert len(products) == 20
