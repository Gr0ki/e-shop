"""Contains v1 of the api views related to the OrderItem model."""

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .....orders.models import OrderItem, Order
from .....orders.serializers import OrderItemSerializer


class OrderItemList(ListAPIView):
    """
    Provides GET method for the listing of all the Statuses.
    Access is allowed only to admin users.
    """

    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff is False:
            self.queryset = self.queryset.filter(order__customer=user.id)
        return super().get_queryset()


class OrderItemCreate(CreateAPIView):
    """
    Provides POST method for creating a new OrderItem.
    Access is allowed only to authenticated users.
    Non-admin users can't specify Orders that don't belong to them.
    """

    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Preventing non-admin users form specifying orders that don't belong to them.
        """
        user = self.request.user
        if (
            user.is_staff is False
            and int(request.data["order"])
            != Order.objects.all().filter(customer_id__id=user.id).first().id
        ):
            raise PermissionDenied()
        return super().create(request, *args, **kwargs)


class OrderItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Provides GET method for detailed OrderItem [for authenticated user].
    An authenticated user can retrieve only an OrderItem that belongs to him/her.

    Provides PUT, PATCH and DELETE methods for detailed OrderItem [for admin users only].
    """

    queryset = OrderItem.objects.all()
    lookup_field = "id"
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        """
        Filters queryset for non-admin users
        to instantiate only those OrderItems that belong to the current user.
        """
        user = self.request.user
        if user.is_staff is False:
            self.queryset = self.queryset.filter(order__customer=user.id)
        return super().get_queryset()

    def check_permissions(self, request):
        """
        Skips inherited implementation of 'check_permissions' for GET method requests.
        """
        if request.method != "GET":
            return super().check_permissions(request)
        return None
