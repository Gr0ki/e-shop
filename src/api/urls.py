from django.urls import include, path

from .api_routes_lists_documentation.views import APIVersionsRoutesList


urlpatterns = [
    path("", APIVersionsRoutesList.as_view(), name="api-versions-routes"),
    path("v1/", include("src.api.v1.urls"), name="v1"),
]
