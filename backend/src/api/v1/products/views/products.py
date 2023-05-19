"""Contains v1 of the api views related to the Product model."""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from .....products.models import Product
from .....products.serializers import ProductSerializer


class ProductList(ListAPIView):
    """
    Provides GET method for the listing of all the Products,
    supports filtering on fields 'category' and 'is_in_stock',
    supports searching on fields 'name' and 'description'.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("category", "is_in_stock")
    search_fields = ("name", "description")


class ProductCreate(CreateAPIView):
    """
    Provides POST method for creating a new Product.
    Access is allowed only to admin users.
    """

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        """Adds additional validational layer."""
        price = request.data.get("price")
        if not isinstance(price, float):
            try:
                price = float(price)
            except ValueError:
                raise ValidationError(
                    {"price": "A valid float number above 0.0 is required."}
                )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})

        return super().create(request, *args, **kwargs)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Provides GET method for detailed Product [accessible for everyone].
    Provides PUT, PATCH and DELETE methods for detailed Product [for admin users only].
    """

    queryset = Product.objects.all()
    lookup_field = "id"
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def check_permissions(self, request):
        """
        Skips inherited implementation of 'check_permissions' for GET method requests.
        """
        if request.method != "GET":
            return super().check_permissions(request)
        return None

    def update(self, request, *args, **kwargs):
        """
        Adds additional validational layer.
        """
        price = request.data.get("price")
        if not isinstance(price, float):
            raise ValidationError(
                {"price": "A valid float number above 0.0 is required."}
            )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})

        return super().update(request, *args, **kwargs)
