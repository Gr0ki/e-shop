"""Contains v1 of the api views related to the Order model."""

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


from .....orders.models import Order
from .....orders.serializers import OrderSerializer


class OrderList(ListAPIView):
    """
    Provides GET method for the listing of all
    the Orders for the current logged-in user.

    Allows staff personnel to get Orders for all users
    and filter the list of Orders on the field 'customer'.

    Access allowed only to authenticated users.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("customer",)

    def filter_queryset(self, queryset):
        """
        Restricts filter access for not staff users
        before applying the inherited 'filter_queryset' method.
        """
        user = self.request.user
        if not user.is_staff:
            self.filter_backends = []
        return super().filter_queryset(queryset)

    def get_queryset(self):
        """
        Limits queryset for not staff users
        by filtering the result for current logged-in user only,

        then apply the inherited 'get_queryset' method.
        """
        user = self.request.user
        if user.is_staff is False:
            self.queryset = self.queryset.filter(customer=user.id)
        return super().get_queryset()


class OrderCreate(CreateAPIView):
    """
    Provides POST method for creating a new Order.
    Access is allowed only to authenticated users.
    """

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Adds restriction for authenticated user
        to create a new Order with specifying request data explicitly.
        """
        user = self.request.user
        if user.is_staff is False and len(request.data) == 0:
            request.data["customer"] = user.id
        elif user.is_staff is False and len(request.data) != 0:
            raise PermissionDenied()
        return super().create(request, *args, **kwargs)


class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Provides GET method for detailed Order [for authenticated user].
    An authenticated user can retrieve only an Order that belongs to him/her.

    Provides PUT, PATCH and DELETE methods for detailed Order [for admin users only].
    """

    queryset = Order.objects.all()
    lookup_field = "id"
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        """
        Gives access for non-admin user for GET method requests
        by rewriting permission_classes field.
        """
        user = self.request.user
        request_method = self.request.method
        if request_method == "GET" and user.is_authenticated is True:
            self.permission_classes = []

        return super().get_permissions()

    def get_queryset(self):
        """
        Filters queryset for non-admin users
        to instantiate only those Orders that belong to the current user.
        """
        user = self.request.user
        request_method = self.request.method

        if user.is_authenticated is True and user.is_staff is False:
            self.queryset = self.queryset.filter(customer=user.id)
        return super().get_queryset()
