from django.urls import path

from .views import *


urlpatterns = [
    path('products', ProductList.as_view(), name='products-list'),
    path('products/new', ProductCreate.as_view(), name='add-new-product'),
    path('products/<int:id>', ProductRetrieveUpdateDestroy.as_view(), name='product-rud'),

]
