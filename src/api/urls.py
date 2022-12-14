from django.urls import include, path

from .docs.views import APIVersionsRoutesList
from ..products.api.urls import urlpatterns as products_api_urlpatterns
from ..orders.api.urls import urlpatterns as orders_api_urlpatterns


urlpatterns = [
    path("", APIVersionsRoutesList.as_view(), name="api-versions-routes"),
    path("v1/", include(("src.api.docs.v1.urls", "docs"), namespace="docs")),
    path(
        "v1/",
        include(
            (orders_api_urlpatterns + products_api_urlpatterns, "api"), namespace="v1"
        ),
    ),
]
