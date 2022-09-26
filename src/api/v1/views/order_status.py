from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from ....orders.models import Status
from ....orders.serializers import StatusSerializer


class StatusList(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusCreate(CreateAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    lookup_field = "id"
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]
