from django.urls import path
from custom_perfil.views import custom_perfil, update_profile

urlpatterns = [
        path('', custom_perfil, name='custom_perfil'),
        path('update/', update_profile, name='update_profile'),
]