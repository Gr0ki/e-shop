from django.urls import path

from .views import *


urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_request, name='register'),
    path('change_password/', change_password_request, name='change_password')
]