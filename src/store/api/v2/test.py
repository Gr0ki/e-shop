from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        """
        Tests if creating a new Product object is possible.
        """
        initial_product_count = Product.objects.count()
        url = reverse('add-new-product')
        data = {
            "name": "New product",
            "price": 500.0,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), initial_product_count + 1)

        for key, expected_value in data.items():
            self.assertEqual(response.data[key], expected_value)

        if 'is_in_stock' not in data.keys():
            self.assertEqual(response.data['is_in_stock'], True)
