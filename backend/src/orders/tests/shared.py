"""Contains shared code for orders related tests."""

from faker import Faker

from datetime import datetime
from django.utils.timezone import get_current_timezone


fake = Faker()


def convert_datetime_to_str_timestamp(datetime_instace: datetime) -> str:
    """Converts datetime instance to string timestamp."""
    return datetime_instace.astimezone(get_current_timezone()).isoformat()
