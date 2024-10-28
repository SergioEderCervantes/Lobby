from django.urls import path
from restaurante.views import restaurante

urlpatterns = [
    path('', restaurante, name='restaurante'),
]