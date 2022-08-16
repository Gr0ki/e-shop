from rest_framework import serializers


# from ..orders.models import OrderItem
# from ..orders.serializers import OrderItemSerializer
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class ProductSerializer(serializers.ModelSerializer):
    # TODO: add authorization for stat fields
    # ordered_quantity = serializers.SerializerMethodField()
    # carts_items_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "category",
            "description",
            "is_in_stock",
            # "ordered_quantity",
            # "carts_items_quantity",
        )

    # def get_ordered_quantity(self, instance):
    #     items = OrderItem.objects.filter(product=instance, order__isnull=False)
    #     data = OrderItemSerializer(items, many=True).data
    #     if data:
    #         return sum((item["quantity"] for item in data))
    #     else:
    #         return 0

    # def get_carts_items_quantity(self, instance):
    #     items = OrderItem.objects.filter(product=instance, order__isnull=True)
    #     data = OrderItemSerializer(items, many=True).data
    #     if data:
    #         return sum((item["quantity"] for item in data))
    #     else:
    #         return 0
