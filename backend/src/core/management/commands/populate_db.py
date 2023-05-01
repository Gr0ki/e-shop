"""CLI commands for populating database."""
from django.core.management.base import BaseCommand

from ....accounts.factories import UserFactory
from ....orders.factories import StatusFactory, OrderFactory, OrderItemFactory
from ....products.factories import CategoryFactory, ProductFactory


class Command(BaseCommand):
    """Populates db with random data."""

    help = "Populates db tables with fake data."

    def handle(self, *args, **options):
        UserFactory.create_batch(5)
        StatusFactory.create_batch(3)
        OrderFactory.create_batch(40)
        CategoryFactory.create_batch(4)
        ProductFactory.create_batch(20)
        OrderItemFactory.create_batch(60)
        self.stdout.write("Database was successfuly populated!")
