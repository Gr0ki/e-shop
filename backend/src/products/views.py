"""Contains products app views."""

from django.views.generic import TemplateView


class ProductsView(TemplateView):
    """View for the products page."""

    template_name = "products/products.html"
