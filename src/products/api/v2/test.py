from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from src.products.api.v2.serializers import ProductSerializer
from ...models import Product


class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        """
        Tests if creating a new Product object is possible.
        """
        initial_product_count = Product.objects.count()
        url = reverse("add-new-product")
        data = {
            "name": "New product",
            "price": 500.0,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), initial_product_count + 1)

        for key, expected_value in data.items():
            self.assertEqual(response.data[key], expected_value)

        if "is_in_stock" not in data.keys():
            self.assertEqual(response.data["is_in_stock"], True)


class ProductDestroyTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name="New product2", price=9888.5)

    def test_delete_product(self):
        """
        Tests if destroying a Product object is possible.
        """
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        url = reverse("product-rud", args=(product_id,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), initial_product_count - 1)
        self.assertRaises(Product.DoesNotExist, Product.objects.get, id=product_id)


class ProductListTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name="New product3", price=544.5)
        Product.objects.create(name="New product4", price=523.5)

    def test_products_list(self):
        """
        Tests if geting a list of Products is possible.
        """
        products = Product.objects.all()
        url = reverse("products-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(products))


class ProductUpdateTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name="New product5", price=10.9)
        Product.objects.create(name="New product7", price=500.9)

    def test_product_update_put(self):
        """
        Tests if updating a list of Products is possible with a put method.
        """
        product = Product.objects.first()
        url = reverse("product-rud", args=(product.id,))
        data_to_update = {"name": "New product6", "price": 100.9}
        response = self.client.put(url, data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for key, expected_value in data_to_update.items():
            self.assertEqual(response.data[key], expected_value)
        self.assertEqual(response.data["name"], Product.objects.get(id=product.id).name)
        self.assertEqual(
            response.data["price"], Product.objects.get(id=product.id).price
        )

    def test_product_update_patch(self):
        """
        Tests if updating a list of Products is possible with a patch method.
        """
        product = Product.objects.get(name="New product7")
        url = reverse("product-rud", args=(product.id,))
        data_to_update = {"name": "New product8"}
        response = self.client.patch(url, data_to_update)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for key, expected_value in data_to_update.items():
            self.assertEqual(response.data[key], expected_value)
        self.assertEqual(response.data["name"], Product.objects.get(id=product.id).name)
