from rest_framework.generics import ListAPIView

from .serializers import ProductSerializer
from ...models import Product


class ProductList(ListAPIView):
    '''
    Returns a list of all products.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
