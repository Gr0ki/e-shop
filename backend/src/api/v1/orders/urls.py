"""Contains urlpatterns for v1 of the api endpoints related to the orders app."""

from django.urls import path

from .views.orders_statuses import StatusList, StatusCreate, StatusRetrieveUpdateDestroy
from .views.orders import OrderList, OrderCreate, OrderRetrieveUpdateDestroy
from .views.oders_items import (
    OrderItemList,
    OrderItemCreate,
    OrderItemRetrieveUpdateDestroy,
)


urlpatterns = [
    # Orders Statuses:
    path("order-statuses", StatusList.as_view(), name="status-list"),
    path("order-statuses/new", StatusCreate.as_view(), name="add-new-status"),
    path(
        "order-statuses/<int:id>",
        StatusRetrieveUpdateDestroy.as_view(),
        name="status-rud",
    ),
    # Orders:
    path("orders", OrderList.as_view(), name="order-list"),
    path("orders/new", OrderCreate.as_view(), name="add-new-order"),
    path("orders/<int:id>", OrderRetrieveUpdateDestroy.as_view(), name="order-rud"),
    # Orders Items:
    path("orders-items", OrderItemList.as_view(), name="order-item-list"),
    path("orders-items/new", OrderItemCreate.as_view(), name="add-new-order-item"),
    path(
        "orders-items/<int:id>",
        OrderItemRetrieveUpdateDestroy.as_view(),
        name="order-item-rud",
    ),
]
