from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path("admin/", admin.site.urls, name="admin"),
    path("account/", include("src.accounts.urls")),
    path("api/", include("src.api.urls")),
    path("", include("src.products.urls")),
    path("products/", include("src.products.urls")),
    path("orders/", include("src.orders.urls")),
]
