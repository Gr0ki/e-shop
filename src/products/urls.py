from django.urls import path

from .views import *


urlpatterns = [
    path("", ProductsView.as_view(), name="products-list-page"),
]