from django.shortcuts import render
from django.http import JsonResponse
from .services import crearMatch
# Create your views here.

class Tournament(object):
    def __init__(self,id, name, date, players):
        self.id = id
        self.name = name
        self.date = date
        self.players = players


def tournaments(request):
    tournaments = [
        Tournament(1, 'Tournament 1', '2021-10-01', 10),
        Tournament(2, 'Tournament 2', '2021-10-02', 20),
        Tournament(3, 'Tournament 3', '2021-10-03', 30),
    ]

    return render(request, 'tournaments.html', {'tournaments': tournaments})

def tournament_matches(request):
    data = crearMatch([1, 2, 3, 4, 5, 6, 7, 8])
    matches = [{'id': match.id, 'player1': match.player1, 'player2': match.player2} for match in data]
    return JsonResponse({'matches': matches})