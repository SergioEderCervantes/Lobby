from django.shortcuts import render
from tournaments.models import Tournament_prueba, Users_prueba
from custom_admin.services import crearMatch
from django.shortcuts import get_object_or_404  

# Create your views here.

class Tournament(object):
    def __init__(self,id, name, date, players):
        self.id = id
        self.name = name
        self.date = date
        self.players = players

def object_view(request, object_id):
    objeto = get_object_or_404(Tournament_prueba,pk=object_id)
    tournament = Tournament(objeto.tournament_id, objeto.tournament_name, objeto.date,10)
    matches = None
    is_ideal = False
    if request.method == "POST":
        players = list(Users_prueba.objects.filter(tournament_id = tournament.id).values_list('first_name', flat=True))
        print(players)
        data, is_ideal = crearMatch(players)
        matches = [{'id': match.id, 'player1': match.player1, 'player2': match.player2} for match in data]

    return render(request, 'admin/object_view.html', {'tournament' : tournament, 'matches': matches,
                                                       'object_id': object_id, 'is_ideal':is_ideal})