from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer
from ...models import Product


class ProductList(ListAPIView):
    '''
    Returns a list of all products.
    Enabled filter result by id (?id=1).
    Enabled search by name and description for a partial match (?search=example).
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', )
    search_fields = ('name', 'description')
