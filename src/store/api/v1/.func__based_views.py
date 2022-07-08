from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ...models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def view_list_product(request):
    items = Product.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def add_new_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
