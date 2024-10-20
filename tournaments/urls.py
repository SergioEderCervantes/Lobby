from django.urls import path
from tournaments.views import tournaments
urlpatterns = [
    path('', tournaments, name='tournaments'),
]
