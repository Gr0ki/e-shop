"""Contains serializers for the products app."""

from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer."""

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer."""

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "category",
            "description",
            "is_in_stock",
        )
