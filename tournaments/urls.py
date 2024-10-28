from django.urls import path
from tournaments.views import tournaments, tournament_detail
urlpatterns = [
    path('', tournaments, name='tournaments'),
    path('<str:name>/', tournament_detail, name='tournament_detail'),
]
