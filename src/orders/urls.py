from django.urls import path

from .views import *


urlpatterns = [
    path("", OrdersView.as_view(), name="orders-list-page"),
]
