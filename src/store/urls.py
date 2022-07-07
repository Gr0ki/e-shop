from django.urls import path, include

from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('api/', include('src.store.api.urls')),
    
]
