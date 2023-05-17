"""Contains shared code for product related tests."""

from faker import Faker


fake = Faker()

CATEGORY_NAME = fake.word()
PRODUCT_NAME = fake.word()
IS_IN_STOCK = fake.boolean()
