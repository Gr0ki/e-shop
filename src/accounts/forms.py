from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]    


class AuthUserForm(AuthenticationForm):
    pass


class ChangePasswordForm(PasswordChangeForm):
    pass
