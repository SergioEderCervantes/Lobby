from django.urls import path
from reservations.views import reservations

urlpatterns = [
    path('', reservations, name='reservations'),
]