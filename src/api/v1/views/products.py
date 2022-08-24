from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from ....products.models import Product
from ....products.serializers import ProductSerializer


class ProductList(ListAPIView):
    """
    Returns a list of all products.
    Enabled filter result by "id"(?id=1) and "is_in_stock"(?is_in_stock=true) fields.
    Enabled search by name and description for a partial match (?search=example).
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("category", "is_in_stock")
    search_fields = ("name", "description")


class ProductCreate(CreateAPIView):
    """
    Endpoint for staff users only.
    Creates new Product.
    """

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        """
        Validates "price" field for being float and greater than 0.0.
        Returns inherited create method from a parent class.
        """
        price = request.data.get("price")
        if not isinstance(price, float):
            raise ValidationError(
                {"price": "A valid float number above 0.0 is required."}
            )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})
        else:
            return super().create(request, *args, **kwargs)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Everyone has access to the GET method, while others are for staff users only.
    Retrieves, updates and deletes a specific product.
    """

    queryset = Product.objects.all()
    lookup_field = "id"
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        if request.method != "GET":
            super().check_permissions(request)

    def update(self, request, *args, **kwargs):
        """
        Validates "price" field for being float and greater than 0.0.
        Returns inherited update method from a parent class.
        """
        price = request.data.get("price")
        if not isinstance(price, float):
            raise ValidationError(
                {"price": "A valid float number above 0.0 is required."}
            )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})
        else:
            return super().update(request, *args, **kwargs)
