from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from django.core.cache import cache

from ....products.serializers import CategorySerializer
from ....products.models import Category


class CategoryList(ListAPIView):
    """
    Returns a list of all categories.
    Enabled filter result by "id"(?id=1) and "is_in_stock"(?is_in_stock=true) fields.
    Enabled search by name and description for a partial match (?search=example).
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    """
    Creates new Category.
    """

    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates and deletes a specific category.
    Updates the cache with each update or delete action.
    """

    queryset = Category.objects.all()
    lookup_field = "id"
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        """
        Deletes cache data about the specific category.
        Executes delete method from a parent class and returns a response on this action.
        """
        category_id = request.data.get("id")
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            cache.delete("product_data_{}".format(category_id))
        return response

    def update(self, request, *args, **kwargs):
        """
        Updates category.
        Updates the cache.
        """
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            category = response.data
            cache.set(
                "category_data_{}".format(category["id"]),
                {
                    "name": category["name"],
                },
            )
        return response
