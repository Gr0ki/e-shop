from django.urls import path

from .views import *


urlpatterns = [
    # path('product_list', view_list_product, name='product-list'),
    path('products', ProductList.as_view(), name='products-list'),
    # path('product/<int:product_id>', product, name='product'),
    # path('add_new_product', add_new_product, name='add-new-product'),
    path('products/new', ProductCreate.as_view(), name='add-new-product'),
    path('products/<int:id>', ProductRetrieveUpdateDestroy.as_view(), name='product-rud'),

]
