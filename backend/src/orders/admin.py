"""Contains settings for the orders app admin panel."""

from django.contrib import admin

from .models import Status, Order, OrderItem


admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderItem)
