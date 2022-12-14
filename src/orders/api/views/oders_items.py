# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from ...models import OrderItem, Order
from ...serializers import OrderItemSerializer


class OrderItemList(ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ("order",)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff is False:
            # TODO: return 403 error for access attempt for different user's order
            self.queryset = self.queryset.filter(order__customer=user.id)
        return super().get_queryset()


class OrderItemCreate(CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if (
            user.is_staff is False
            and int(request.data["order"])
            != Order.objects.all().filter(customer_id__id=user.id).first().id
        ):
            raise PermissionDenied()
        return super().create(request, *args, **kwargs)


class OrderItemRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    lookup_field = "id"
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff is False:
            self.queryset = self.queryset.filter(order__customer=user.id)
        return super().get_queryset()

    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        if request.method != "GET":
            return super().check_permissions(request)
