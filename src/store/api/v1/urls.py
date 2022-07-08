from django.urls import path

from .views import *


urlpatterns = [
    path('products', list_products, name='product-list'),
    path('products/<int:product_id>', product_detailed, name='product'),
    path('products/new', add_new_product, name='add-new-product'),

]
