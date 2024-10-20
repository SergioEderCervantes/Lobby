from django.shortcuts import render
from tournaments.models import Tournament_prueba
from custom_admin.services import crearMatch
from django.http import JsonResponse

# Create your views here.

class Tournament(object):
    def __init__(self,id, name, date, players):
        self.id = id
        self.name = name
        self.date = date
        self.players = players

def object_view(request, object_id):
    objeto = Tournament_prueba.objects.get(tournament_id = object_id);
    if not objeto:
        print("ERROR ERROR")
        # TODO: mandar un 404
    else:
        tournament = Tournament(objeto.tournament_id, objeto.tournament_name, objeto.date,10)
        return render(request, 'admin/object_view.html', {'tournament' : tournament})
        
        
def tournament_matches(request, object_id):
    data = crearMatch([1, 2, 3, 4, 5, 6, 7, 8])
    matches = [{'id': match.id, 'player1': match.player1, 'player2': match.player2} for match in data]
    return JsonResponse({'matches': matches})