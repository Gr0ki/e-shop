from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
import requests

from config.settings import GOOGLE_RECAPTCHA_SITE_KEY, GOOGLE_RECAPTCHA_SECRET_KEY
from .forms import *


class AccountView(LoginRequiredMixin, TemplateView):
    template_name='accounts/account_page.html'
    login_url='login/'


def register_request(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            ''' reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
                ''' if reCAPTCHA returns True '''
                form.save()
                return redirect('login')
            else: 
                ''' if reCAPTCHA returns False '''
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    context = {'form': form, 'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, 'registration/register.html', context)


def login_request(request):
    form = AuthUserForm()

    if request.method == 'POST':
        form = AuthUserForm(request, data=request.POST)

        ''' reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            ''' if reCAPTCHA returns True '''
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account')
                else:
                    messages.info(request, 'User has been banned.')
            else:
                messages.info(request, 'Username or password is incorrect.')
        else: 
            ''' if reCAPTCHA returns False '''
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    form = AuthUserForm()
    context = {'form': form, 'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, 'registration/login.html', context)


def logout_request(request):
    logout(request)
    return redirect("welcome")

@login_required
def change_password_request(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            ''' reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
                ''' if reCAPTCHA returns True '''
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('account')
            else: 
                ''' if reCAPTCHA returns False '''
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    else:
        form = ChangePasswordForm(request.user)
    context = {'form': form, 'recaptcha_site_key': GOOGLE_RECAPTCHA_SITE_KEY}
    return render(request, 'registration/change_password.html', context)
