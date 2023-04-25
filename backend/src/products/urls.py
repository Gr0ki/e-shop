from django.urls import path

from .views import ProductsView


urlpatterns = [
    # Products template:
    path("", ProductsView.as_view(), name="products-list-page"),
]
