from django.shortcuts import render
from custom_admin.views import Tournament
from .models import Torneo
from django.shortcuts import get_object_or_404 
import os
from settings import STATICFILES_DIRS 

# Create your views here.

def tournaments(request):
    data = Torneo.objects.all()
    tournaments = [Tournament(t.nombre_torneo,t.nombre_juego,"",t.fecha,"","",t.usuarios_torneo.all().count()) for t in data]


    return render(request, 'tournaments.html', {'tournaments': tournaments})


def tournament_detail(request, name):
    torneo = get_object_or_404(Torneo,nombre_torneo=name)
    matchups_ready = torneo.is_defined
    svg_data = None
    if(matchups_ready):
        parent_dir = STATICFILES_DIRS[0]
        file_name= str(torneo.pk) + '.svg'
        file_path = os.path.join(parent_dir,'svg_tournaments', file_name)
        with open(file_path, 'r') as svg_file:
            svg_data = svg_file.read()
            
    # Sacar solo la data del torneo necesaria para el render del html
    tournament_data = Tournament(torneo.nombre_torneo,torneo.nombre_juego,torneo.get_modo_torneo_display(),
                                 torneo.fecha, torneo.descripcion, torneo.reglas.splitlines(),
                                 torneo.usuarios_torneo.all().count())
    
    raw_users = torneo.usuarios_torneo.all()
    
    players = [user.username for user in raw_users]
    print(len(players))
    return render(request, 'tournament_detail.html', {'tournament' : tournament_data,'svg_data': svg_data, 'players': players})
