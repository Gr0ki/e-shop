"""Tests Orders views."""

from django.urls import reverse


def test_success_retrival_code_on_orders_list_page(client):
    """Tests successful GET request to orders-list-page."""
    url = reverse("orders-list-page")
    response = client.get(url)
    assert response.status_code == 200
