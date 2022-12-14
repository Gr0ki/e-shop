from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


versions_data = {
    "account-page": "http://127.0.0.1:8000/account/",
    "v1": "http://127.0.0.1:8000/api/v1/",
}


class APIVersionsRoutesList(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        return Response(versions_data, 200)