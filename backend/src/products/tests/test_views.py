"""Tests Products views."""

from django.urls import reverse


def test_success_retrival_code_on_products_list_page(client):
    """Tests successful GET request to products-list-page."""
    url = reverse("products-list-page")
    response = client.get(url)
    assert response.status_code == 200
