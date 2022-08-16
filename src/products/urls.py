from django.urls import path, include

from .views import *


urlpatterns = [
    path("", ProductsView.as_view(), name="main"),
    path("api/", include("src.products.api.urls")),
]
