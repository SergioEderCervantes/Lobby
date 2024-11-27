from django.urls import path
from cookies_servicios.views import cookies_servicios

urlpatterns = [
        path('', cookies_servicios, name='cookies_servicios'),
]