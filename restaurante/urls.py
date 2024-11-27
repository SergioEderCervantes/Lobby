from django.urls import path
from restaurante.views import restaurante, prueba

urlpatterns = [
    path('', restaurante, name='restaurante'),
    path('prueba/', prueba, name='prueba')
]