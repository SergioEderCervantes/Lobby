from django.urls import path
from custom_perfil.views import custom_perfil

urlpatterns = [
        path('', custom_perfil, name='custom_perfil'),
]