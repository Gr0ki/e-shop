"""Tests Accounts views."""

import pytest
from django.urls import reverse


@pytest.mark.parametrize("param", ("login", "register"))
def test_success_retrival_code_on_accounts_pages(client, param):
    """Tests successful GET request to account pages."""
    url = reverse(param)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "url_name,redirect_url",
    (
        ("account", "/account/login/?next=/account/"),
        ("logout", reverse("orders-list-page")),
        ("change_password", "/account/login/?next=/account/change_password/"),
    ),
)
def test_redirect_on_retrival_for_accounts_pages(client, url_name, redirect_url):
    """Tests redirect on GET request to account pages."""
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == redirect_url
