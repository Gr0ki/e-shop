from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from ...models import Product
from ...serializers import ProductSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("category", "is_in_stock")
    search_fields = ("name", "description")


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        price = request.data.get("price")
        if not isinstance(price, float):
            try:
                price = float(price)
            except:
                raise ValidationError(
                    {"price": "A valid float number above 0.0 is required."}
                )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})
        else:
            return super().create(request, *args, **kwargs)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "id"
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def check_permissions(self, request):
        if request.method != "GET":
            super().check_permissions(request)

    def update(self, request, *args, **kwargs):
        price = request.data.get("price")
        if not isinstance(price, float):
            raise ValidationError(
                {"price": "A valid float number above 0.0 is required."}
            )
        if price <= 0.0:
            raise ValidationError({"price": "Must be above 0.0."})
        else:
            return super().update(request, *args, **kwargs)
