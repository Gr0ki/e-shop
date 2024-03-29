"""Contains urlpatterns for v1 of the api endpoints related to the products app."""

from django.urls import path

from .views.products_categories import (
    CategoryList,
    CategoryCreate,
    CategoryRetrieveUpdateDestroy,
)
from .views.products import ProductList, ProductCreate, ProductRetrieveUpdateDestroy


urlpatterns = [
    # Products Categories:
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
]
