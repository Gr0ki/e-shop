from django.urls import path, include


urlpatterns = [
    path('v1/', include('src.store.api.v1.urls')),
    path('v2/', include('src.store.api.v2.urls')),
    
]