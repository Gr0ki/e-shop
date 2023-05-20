"""Contains settings for the products app admin panel."""

from django.contrib import admin

from .models import Category, Product


admin.site.register(Category)
admin.site.register(Product)
