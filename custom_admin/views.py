import os
import json
from django.shortcuts import render
from tournaments.models import Tournament_prueba, Users_prueba
from custom_admin.services import crearMatch
from django.shortcuts import get_object_or_404  
from django.http import JsonResponse
from settings import STATICFILES_DIRS
from django.views.decorators.csrf import csrf_exempt
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
    matchups_ready = objeto.matchups_ready
    svg_data = None
    matches = None
    is_ideal = False
    # Si ya los matchups estan hechos, carga el svg y lo manda sin mas 
    if (matchups_ready):
        parent_dir = STATICFILES_DIRS[0]
        file_name= str(tournament.id) + '.svg'
        file_path = os.path.join(parent_dir,'svg', file_name)
        with open(file_path, 'r') as svg_file:
            svg_data = svg_file.read()
    # Si no estan los matchups pero el request es post, manda la informacion para hacerlos  
    elif request.method == "POST":      
        players = list(Users_prueba.objects.filter(tournament_id = tournament.id).values_list('first_name', flat=True))
        data, is_ideal = crearMatch(players)
        matches = [{'id': match.id, 'player1': match.player1, 'player2': match.player2} for match in data]

    return render(request, 'admin/object_view.html', {'torneo_id':object_id, 'tournament': tournament, 'matchups_ready':matchups_ready,
                                                       'svg_data':svg_data,'matches':matches,'is_ideal':is_ideal})

def save_svg(request):
    if (request.method != 'POST'):
        return JsonResponse({'status': 'error', 'message':'metodo no permitido'}, status=405)
    body_unicode = request.body.decode('utf-8')
    try:
        data = json.loads(body_unicode)
    except:
        return JsonResponse({'error': 'No se pudo decodificar el JSON'}, status=400)   
    print(f"Data:{data}")
    svg_data = data.get('svg_data')
    torneo_id = data.get('torneo_id')
    if not svg_data or torneo_id == 0:
        return JsonResponse({'status': 'error', 'message':'No se pudo encontrar la data o se entrego un id = 0'}, status=400)
    try:
        file_name= str(torneo_id) + '.svg'
        parent_dir = STATICFILES_DIRS[0]
        file_path = os.path.join(parent_dir,'svg',file_name)
        with open(file_path,'w') as file:
            file.write(svg_data)
        
        tournament = Tournament_prueba.objects.get(pk=torneo_id)
        tournament.matchups_ready = True
        tournament.save()
    except Exception as e:
        print(e)
        print("Algo sucedio mal, variables usadas:")
        print(f"torneo_id:{torneo_id}")
        print(f"svg Data:{svg_data}")
        return JsonResponse({'status': 'error', 'message':'Hubo un problema al intentar guardar el svg'}, status=400)
    return JsonResponse({'status': 'success', 'message': 'SVG guardado correctamente.'})
