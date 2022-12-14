from django.urls import path

from .views import *


urlpatterns = [
    # API routes:
    path("", APIV1RoutesList.as_view(), name="api-v1-routes"),

]
