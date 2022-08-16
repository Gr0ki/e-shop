from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"Category: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    # image = models.ImageField()
    category = models.OneToOneField(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(null=True, blank=True)
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"Product name: {self.name}. Price: {self.price}. Is in stock: {self.is_in_stock}."
