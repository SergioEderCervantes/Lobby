from django.urls import path
from politicas.views import politicas
urlpatterns = [
        path('', politicas, name='politicas'),
]