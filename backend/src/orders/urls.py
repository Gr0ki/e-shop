"""Contains urlpatterns for orders app views."""

from django.urls import path

from .views import OrdersView


urlpatterns = [
    # Orders template:
    path("", OrdersView.as_view(), name="orders-list-page"),
]
