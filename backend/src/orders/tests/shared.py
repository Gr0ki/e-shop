"""Contains shared code for orders related tests."""

from datetime import datetime
from faker import Faker
from django.utils.timezone import get_current_timezone


fake = Faker()

STATUS_NAME = fake.word()
TEST_USERNAME = fake.word()
PRODUCT_NAME = fake.word()


def convert_datetime_to_str_timestamp(datetime_instace: datetime) -> str:
    """Converts datetime instance to string timestamp."""
    return datetime_instace.astimezone(get_current_timezone()).isoformat()
