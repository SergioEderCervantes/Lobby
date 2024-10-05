from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

# Tournaments

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