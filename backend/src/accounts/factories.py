"""Contains the User Factory for the standard Django user model."""
from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory
from factory import sequence, LazyAttribute, PostGenerationMethodCall


class UserFactory(DjangoModelFactory):
    """User Factory for default Django User model."""

    class Meta:
        model = get_user_model()
        # django_get_or_create = ["username"]

    email = LazyAttribute(lambda o: f"{o.username}@example.com")
    password = PostGenerationMethodCall("set_password", "password")

    @sequence
    def username(_):
        try:
            max_id = get_user_model().objects.latest("id").id
            return f"user-{max_id + 1}"
        except get_user_model().DoesNotExist:
            return f"user-0"
