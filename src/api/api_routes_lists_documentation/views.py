from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

v1_data = {
    "Product Categories list": "http://127.0.0.1:8000/api/v1/categories",  # guest, customer
    "Add new product category": "http://127.0.0.1:8000/api/v1/categories/new",  # staff
    "Product Category detailed": "http://127.0.0.1:8000/api/v1/categories/1",  # staff
    # __________
    "Products list": "http://127.0.0.1:8000/api/v1/products",  # guest, customer, staff
    "Add new product": "http://127.0.0.1:8000/api/v1/products/new",  # staff
    "Product detailed": "http://127.0.0.1:8000/api/v1/products/1",  # GET-(guest, customer, staff), UD(staff)
    # __________
    "Order statuses list": "http://127.0.0.1:8000/api/v1/order-statuses",  # staff
    "Add new order status": "http://127.0.0.1:8000/api/v1/order-statuses/new",  # staff
    "Order status detailed": "http://127.0.0.1:8000/api/v1/order-statuses/1",  # staff
    # __________
    "Order list": "http://127.0.0.1:8000/api/v1/orders",  # customer(limited), staff
    "Add new order": "http://127.0.0.1:8000/api/v1/orders/new",  # customer(limited), staff
    "Order detailed": "http://127.0.0.1:8000/api/v1/orders/1",  # customer(limited), staff
    # __________
    "OrderItem list": "http://127.0.0.1:8000/api/v1/order-item",  # customer(limited), staff
    "Add new OrderItem": "http://127.0.0.1:8000/api/v1/order-item/new",  # customer(limited), staff
    "OrderItem detailed": "http://127.0.0.1:8000/api/v1/order-item/1",  # customer(limited), staff
}

versions_data = {
    "account-page": "http://127.0.0.1:8000/account/",
    "v1": "http://127.0.0.1:8000/api/v1/",
}


class APIVersionsRoutesList(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(versions_data, 200)


class APIV1RoutesList(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(v1_data, 200)
