from django.urls import path

from .views import *


urlpatterns = [
    path('products', list_products, name='products-list'),
    path('products/new', add_new_product, name='add-new-product'),
    path('products/<int:id>', product_detailed, name='product-rud'),

]
