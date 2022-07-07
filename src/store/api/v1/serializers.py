from rest_framework import serializers

from ...models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = (
        #     'id', 'name',
        #     'price', 'category',
        #     'description', 'is_in_stock',
        #     )
        fields = ('__all__')
