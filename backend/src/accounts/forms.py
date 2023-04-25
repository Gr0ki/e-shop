from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
        ]


class AuthUserForm(AuthenticationForm):
    pass


class ChangePasswordForm(PasswordChangeForm):
    pass
