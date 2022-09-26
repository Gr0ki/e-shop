from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


from ....orders.models import Order
from ....orders.serializers import OrderSerializer


class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("customer",)

    def filter_queryset(self, queryset):
        user = self.request.user
        if not user.is_staff:
            self.filter_backends = []
        return super().filter_queryset(queryset)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff is False:
            self.queryset = self.queryset.filter(customer=user.id)
        return super().get_queryset()


class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_staff is False and len(request.data) == 0:
            request.data["customer"] = user.id
        elif user.is_staff is False and len(request.data) != 0:
            raise PermissionDenied()
        return super().create(request, *args, **kwargs)


class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    lookup_field = "id"
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        user = self.request.user
        request_method = self.request.method
        if request_method == "GET" and user.is_authenticated is True:
            self.permission_classes = []

        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        request_method = self.request.method

        if (
            user.is_authenticated is True
            and user.is_staff is False
            and request_method == "GET"
        ):
            self.queryset = self.queryset.filter(customer=user.id)
        return super().get_queryset()
