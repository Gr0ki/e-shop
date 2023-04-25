from django.urls import include, path

from .v1.products.urls import urlpatterns as products_api_urlpatterns
from .v1.orders.urls import urlpatterns as orders_api_urlpatterns


urlpatterns = [
    path(
        "v1/",
        include(
            (orders_api_urlpatterns + products_api_urlpatterns, "api"), namespace="v1"
        ),
    ),
]
