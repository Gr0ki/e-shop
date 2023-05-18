"""Contains v1 of the api views related to the Status model."""

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from .....orders.models import Status
from .....orders.serializers import StatusSerializer


class StatusList(ListAPIView):
    """
    Provides GET method for the listing of all the Statuses.
    Access is allowed only to admin users.
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusCreate(CreateAPIView):
    """
    Provides POST method for creating a new Status.
    Access is allowed only to admin users.
    """

    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


class StatusRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Provides GET, PUT, PATCH and DELETE methods for detailed Status.
    Access is allowed only to admin users.
    """

    queryset = Status.objects.all()
    lookup_field = "id"
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]
