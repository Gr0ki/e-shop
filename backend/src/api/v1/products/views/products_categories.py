"""Contains v1 of the api views related to the Category model."""

from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from .....products.models import Category
from .....products.serializers import CategorySerializer


class CategoryList(ListAPIView):
    """
    Provides GET method for the listing of all the Categories,
    supports searching on field 'name'.
    """

    queryset = Category.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    """
    Provides POST method for creating a new Category.
    Access is allowed only to admin users.
    """

    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Provides GET, PUT, PATCH and DELETE methods for detailed Category.
    Access is allowed only to admin users.
    """

    queryset = Category.objects.all()
    lookup_field = "id"
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
