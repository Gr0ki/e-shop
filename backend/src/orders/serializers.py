from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Order, OrderItem, Status


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    # items = PrimaryKeyRelatedField(read_only=True, default=OrderItem())

    class Meta:
        model = Order
        fields = ("id", "customer", "items", "status", "date_time_updated")
