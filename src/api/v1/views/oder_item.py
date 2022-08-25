from django.core.cache import cache
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from ....orders.models import OrderItem
from ....orders.serializers import OrderItemSerializer


class OrderItemList(ListAPIView):
    """
    Endpoint for staff users only.
    Returns a list of all orders items.
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]


class OrderItemCreate(CreateAPIView):
    """
    Endpoint for staff users only.
    Creates new status (for orders model).
    """

    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]


class OrderItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Endpoint for staff users only.
    Retrieves, updates and deletes a specific status (for orders model).
    Updates the cache with each update or delete action.
    """

    queryset = OrderItem.objects.all()
    lookup_field = "id"
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        """
        Deletes cache data about the specific status (for orders model).
        Executes delete method from a parent class and returns a response on this action.
        """
        status_id = request.data.get("id")
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            cache.delete("status_data_{}".format(status_id))
        return response

    def update(self, request, *args, **kwargs):
        """
        Updates status (for orders model).
        Updates the cache.
        """
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            status = response.data
            cache.set(
                "status_data_{}".format(status["id"]),
                {
                    "name": status["name"],
                },
            )
        return response
