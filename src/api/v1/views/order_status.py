from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from ....orders.models import Status
from ....orders.serializers import StatusSerializer


class StatusList(ListAPIView):
    """
    Endpoint for staff users only.
    Returns a list of all statuses (for orders model).
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusCreate(CreateAPIView):
    """
    Endpoint for staff users only.
    Creates new status (for orders model).
    """

    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Endpoint for staff users only.
    Retrieves, updates and deletes a specific status (for orders model).
    """

    queryset = Status.objects.all()
    lookup_field = "id"
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]
