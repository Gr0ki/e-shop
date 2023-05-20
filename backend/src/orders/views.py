"""Contains orders app views."""

from django.views.generic import TemplateView


class OrdersView(TemplateView):
    """View for the orders page."""

    template_name = "orders/orders.html"
