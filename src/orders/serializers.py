from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem, Status


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
