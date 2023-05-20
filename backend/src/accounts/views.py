"""Contains accounts app views."""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
import requests

from config.settings import GOOGLE_RECAPTCHA_SITE_KEY, GOOGLE_RECAPTCHA_SECRET_KEY
from .forms import CreateUserForm, AuthUserForm, ChangePasswordForm


class AccountView(LoginRequiredMixin, TemplateView):
    """View for the account page."""

    template_name = "accounts/account_page.html"
    login_url = "login/"


def register_request(request):
    """Register view."""
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid() is True:
            # reCAPTCHA validation
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            response = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=data,
                timeout=5000,
            )
            result = response.json()

            if result["success"] is True:
                # if reCAPTCHA returns True
                form.save()
                return redirect("login")
            # if reCAPTCHA returns False
            messages.error(request, "Invalid reCAPTCHA. Please try again.")

    context = {"form": form, "recaptcha_site_key": GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, "registration/register.html", context)


def login_request(request):
    """Login view."""
    form = AuthUserForm()

    if request.method == "POST":
        form = AuthUserForm(request, data=request.POST)

        # reCAPTCHA validation
        recaptcha_response = request.POST.get("g-recaptcha-response")
        data = {"secret": GOOGLE_RECAPTCHA_SECRET_KEY, "response": recaptcha_response}
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=data, timeout=5000
        )
        result = response.json()

        if result["success"] is True:
            # if reCAPTCHA returns True
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active is True:
                    login(request, user)
                    return redirect("account")
                messages.info(request, "User has been banned.")
            messages.info(request, "Username or password is incorrect.")
        # if reCAPTCHA returns False
        messages.error(request, "Invalid reCAPTCHA. Please try again.")

    form = AuthUserForm()
    context = {"form": form, "recaptcha_site_key": GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, "registration/login.html", context)


def logout_request(request):
    """Logout view."""
    logout(request)
    return redirect("orders-list-page")


@login_required
def change_password_request(request):
    """Change password view."""
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid() is True:
            # reCAPTCHA validation
            recaptcha_response = request.POST.get("g-recaptcha-response")
            data = {
                "secret": GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": recaptcha_response,
            }
            response = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=data,
                timeout=5000,
            )
            result = response.json()

            if result["success"] is True:
                # if reCAPTCHA returns True
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully updated!")
                return redirect("account")
            # if reCAPTCHA returns False
            messages.error(request, "Invalid reCAPTCHA. Please try again.")
    else:
        form = ChangePasswordForm(request.user)
    context = {"form": form, "recaptcha_site_key": GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, "registration/change_password.html", context)
