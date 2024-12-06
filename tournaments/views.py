import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.db.models import Count
from .models import Torneo
from settings import STATICFILES_DIRS 

# Create your views here.

def tournaments(request):
    tournaments = Torneo.objects.all().annotate(num_players = Count('jugadores_inscritos'))

    return render(request, 'tournaments.html', {'tournaments': tournaments})


def tournament_detail(request, name):
        
    # Obtener el torneo y su número de jugadores inscritos
    torneo = get_object_or_404(Torneo, nombre_torneo=name)

    # Obtener los jugadores inscritos
    players = torneo.usuarios_inscritos()
    num_players = len(players)

    svg_data = None
    if(torneo.is_defined):
        # Carga el SVG
        parent_dir = STATICFILES_DIRS[0]
        file_name= str(torneo.pk) + '.svg'
        file_path = os.path.join(parent_dir,'svg_tournaments', file_name)
        with open(file_path, 'r') as svg_file:
            svg_data = svg_file.read()
            
    context = {
        'torneo': torneo,
        'svg_data': svg_data,
        'reglas': torneo.reglas_como_lista(),
        'num_players': num_players,
        'players': players
    }


    return render(request, 'tournament_detail.html',context)
