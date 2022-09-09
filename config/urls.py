from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("account/", include("src.accounts.urls")),
    path("api/", include("src.api.urls")),
    path("", include("src.products.urls")),
    path("products/", include("src.products.urls")),
    path("orders/", include("src.orders.urls")),
]
