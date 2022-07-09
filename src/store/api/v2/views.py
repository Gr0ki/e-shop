from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from django.core.cache import cache

from .serializers import ProductSerializer
from ...models import Product


class ProductList(ListAPIView):
    '''
    Returns a list of all products.
    Enabled filter result by "id"(?id=1) and "is_in_stock"(?is_in_stock=true) fields.
    Enabled search by name and description for a partial match (?search=example).
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', 'is_in_stock')
    search_fields = ('name', 'description')


class ProductCreate(CreateAPIView):
    '''
    Creates new Product.
    '''
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        '''
        Validates "price" field for being float and greater than 0.0.
        Returns inherited  create method from a parent class.
        '''
        try:
            price = request.data.get('price')
            if not isinstance(price, float):
                raise ValidationError()
        except:
            raise ValidationError(
                {'price': 'A valid float number above 0.0 is required.'}
            )
        if price > 0.0:
            raise ValidationError({'price': 'Must be above 0.0.'})
        else:
            return super().create(request, *args, **kwargs)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    '''
    Retrieves, updates and deletes a specific product.
    Updates the cache with each update or delete action.
    '''
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        '''
        Deletes cache data about the specific product.
        Executes delete method from a parent class and returns a response on this action.
        '''
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self, request, *args, **kwargs):
        '''
        Updates product.
        Updates the cache.
        '''
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            product = response.data
            cache.set('product_data_{}'.format(product['id']),
                      {
                'name': product['name'],
                'price': product['price'],
                'category': product['category'],
                'description': product['description'],
                'is_in_stock': product['is_in_stock']
            })
        return response
