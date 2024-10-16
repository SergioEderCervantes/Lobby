from django.urls import path
from tournaments.views import tournaments, tournament_matches

urlpatterns = [
    path('', tournaments, name='tournaments'),
    path('tournament_matches/', tournament_matches, name='tournament_matches')
]
