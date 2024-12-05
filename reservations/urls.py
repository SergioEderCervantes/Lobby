from django.urls import path
from reservations.views import reservations, check_availability, register_reservation

urlpatterns = [
    path('', reservations, name='reservations'),
    path('check_availability/', check_availability, name="check_availability"),
    path('register_reservation/', register_reservation, name="register_reservation")
]