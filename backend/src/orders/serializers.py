"""Contains serializers for the orders app."""

from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem, Status


class StatusSerializer(ModelSerializer):
    """Status serializer."""

    class Meta:
        model = Status
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    """OrderItem serializer."""

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    """Order serializer."""

    items = OrderItemSerializer(many=True, read_only=True)
    # items = PrimaryKeyRelatedField(read_only=True, default=OrderItem())

    class Meta:
        model = Order
        fields = ("id", "customer", "items", "status", "date_time_updated")
