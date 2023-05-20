# pylint: disable=too-many-ancestors

"""Contains forms for accounts app."""

from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    """Form for creating the user."""

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
        ]


class AuthUserForm(AuthenticationForm):
    """Authentication form."""

    # pylint: disable=unnecessary-pass
    pass


class ChangePasswordForm(PasswordChangeForm):
    """Form for changing user's password."""

    # pylint: disable=unnecessary-pass
    pass
