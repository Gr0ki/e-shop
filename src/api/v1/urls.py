from django.urls import path

from ..api_routes_lists_documentation.views import *
from .views.oder_item import *
from .views.order_status import *
from .views.orders import *
from .views.product_categories import *
from .views.products import *

urlpatterns = [
    # API routes:
    path("", APIV1RoutesList.as_view(), name="api-v1-routes"),
    # Product Categories:
    path("categories", CategoryList.as_view(), name="categories-list"),
    path("categories/new", CategoryCreate.as_view(), name="add-new-category"),
    path(
        "categories/<int:id>",
        CategoryRetrieveUpdateDestroy.as_view(),
        name="category-rud",
    ),
    # Products:
    path("products", ProductList.as_view(), name="products-list"),
    path("products/new", ProductCreate.as_view(), name="add-new-product"),
    path(
        "products/<int:id>", ProductRetrieveUpdateDestroy.as_view(), name="product-rud"
    ),
    # Order Statuses:
    path("order-statuses", StatusList.as_view(), name="status-list"),
    path("order-statuses/new", StatusCreate.as_view(), name="add-new-status"),
    path(
        "order-statuses/<int:id>",
        StatusRetrieveUpdateDestroy.as_view(),
        name="status-rud",
    ),
    # # Orders:
    path("orders", OrderList.as_view(), name="order-list"),
    path("orders/new", OrderCreate.as_view(), name="add-new-order"),
    path("orders/<int:id>", OrderRetrieveUpdateDestroy.as_view(), name="order-rud"),
    # Order Items:
    path("order-item", OrderItemList.as_view(), name="order-item-list"),
    path("order-item/new", OrderItemCreate.as_view(), name="add-new-order-item"),
    path(
        "order-item/<int:id>",
        OrderItemRetrieveUpdateDestroy.as_view(),
        name="order-item-rud",
    ),
]
