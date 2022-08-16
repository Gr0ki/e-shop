from django.urls import path, include


urlpatterns = [
    path("v1/", include("src.products.api.v1.urls")),
    path("v2/", include("src.products.api.v2.urls")),
]
