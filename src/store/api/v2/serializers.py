from rest_framework import serializers

from ...models import Order, OrderItem, Product


class ProductSerializer(serializers.ModelSerializer):
    ordered_quantity = serializers.SerializerMethodField()
    carts_items_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'description',
            'is_in_stock',
            'ordered_quantity',
            'carts_items_quantity'
        )

    def get_ordered_quantity(self, instance):
        items = OrderItem.objects.filter(
            product=instance, order__isnull=False
        )
        data = OrderItemSerializer(items, many=True).data
        if data:
            return sum((item['quantity'] for item in data))
        else:
            return 0

    def get_carts_items_quantity(self, instance):
        items = OrderItem.objects.filter(
            product=instance, order__isnull=True
        )
        data = OrderItemSerializer(items, many=True).data
        if data:
            return sum((item['quantity'] for item in data))
        else:
            return 0


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')
