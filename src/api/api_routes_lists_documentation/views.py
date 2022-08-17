from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

v1_data = {
    "Categories list": "http://127.0.0.1:8000/api/v1/categories",
    "Add new category": "http://127.0.0.1:8000/api/v1/categories/new",
    "Category detailed": "http://127.0.0.1:8000/api/v1/categories/1",
    "Products list": "http://127.0.0.1:8000/api/v1/products",
    "Add new product": "http://127.0.0.1:8000/api/v1/products/new",
    "Product detailed": "http://127.0.0.1:8000/api/v1/products/1",
}

versions_data = {
    "v1": "http://127.0.0.1:8000/api/v1/",
}


class APIVersionsRoutesList(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(v1_data, 200)


class APIV1RoutesList(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(versions_data, 200)
