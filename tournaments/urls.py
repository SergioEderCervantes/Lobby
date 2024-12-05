from django.urls import path
from tournaments.views import tournaments, tournament_detail, register_player, register_guest_player
urlpatterns = [
    path('', tournaments, name='tournaments'),
    path('register_player/', register_player, name= 'register_player'),
    path('register_guest_player/<int:torneo_id>/', register_guest_player, name='register_guest_player'),
    path('<str:name>/', tournament_detail, name='tournament_detail'),
]
