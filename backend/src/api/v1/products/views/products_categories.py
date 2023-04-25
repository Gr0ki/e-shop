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
    queryset = Category.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = "id"
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
