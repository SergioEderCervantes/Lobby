from django.shortcuts import render
from custom_admin.views import Tournament
from .models import Tournament_prueba
from django.shortcuts import get_object_or_404 
import os
from settings import STATICFILES_DIRS 

# Create your views here.




def tournaments(request):
    data = Tournament_prueba.objects.all()
    tournaments = [Tournament(torneo.tournament_id, torneo.tournament_name, torneo.date, 63) for torneo in data]


    return render(request, 'tournaments.html', {'tournaments': tournaments})


def tournament_detail(request, name):
    data = get_object_or_404(Tournament_prueba,tournament_name=name)
    tournament = Tournament(data.tournament_id, data.tournament_name, data.date, 63)
    matchups_ready = data.matchups_ready
    svg_data = None
    if(matchups_ready):
        parent_dir = STATICFILES_DIRS[0]
        file_name= str(tournament.id) + '.svg'
        file_path = os.path.join(parent_dir,'svg', file_name)
        with open(file_path, 'r') as svg_file:
            svg_data = svg_file.read()
    return render(request, 'tournament_detail.html', {'tournament' : tournament,'svg_data': svg_data})
