import os
import json
from tournaments.models import Torneo
from users.models import User
from custom_admin.eliminacion_directa import crearMatch
from custom_admin.round_robin import createRounds
from django.shortcuts import get_object_or_404  
from django.http import JsonResponse
from django.template.response import TemplateResponse
from settings import STATICFILES_DIRS
# Create your views here.

class Tournament(object):
    def __init__(self, name, game_name, mode, date, description, rules, registered_players):
        self.name = name
        self.game_name = game_name
        self.mode = mode
        self.date = date
        self.description = description
        self.rules = rules
        self.registered_players = registered_players

def tournament_view(request, tournament_id):
    # Dios perdoname
    from custom_admin.admin import admin_site
    
    tournament = get_object_or_404(Torneo,pk=tournament_id)
    players = get_registered_players(tournament)
    matchups_ready = tournament.is_defined
    svg_data = None
    parent_dir = STATICFILES_DIRS[0]
    # Si ya los matchups estan hechos, carga el svg y lo manda sin mas 
    if (matchups_ready):
        file_name= str(tournament.pk) + '.svg'
        file_path = os.path.join(parent_dir,'svg_tournaments', file_name)
        with open(file_path, 'r') as svg_file:
            svg_data = svg_file.read()
    # Si no estan los matchups pero el request es post, manda a crear los matchups
    elif request.method == "POST":      
        if(tournament.modo_torneo == 'Direct'):
            file_path = crearMatch(players, tournament.pk, parent_dir=parent_dir)
            # Una vez creado, lo toma desde los archivos y lo guarda en svg_data
        elif tournament.modo_torneo == 'Round':
            file_path = createRounds(players, tournament.pk, parent_dir=parent_dir)
        print(f"File path dado: {file_path}")
        with open(file_path,'r')as svg_file:
            svg_data = svg_file.read()
        matchups_ready = True
        tournament.is_defined = True
        tournament.save()
        
    # Sacar solo la data del torneo necesaria para el render del html
    tournament_data = Tournament(tournament.nombre_torneo,tournament.nombre_juego,tournament.get_modo_torneo_display(),
                                 tournament.fecha, tournament.descripcion, tournament.reglas.splitlines(),
                                 tournament.usuarios_torneo.all().count())
    # Obtener el contexto de custom_admin_site
    context = admin_site.each_context(request)
    
    # Extraer manualmente el app_label y otros detalles
    context.update({
        "title": f"Vista del Torneo: {tournament.nombre_torneo}",
        "torneo_id": tournament_id,
        "tournament": tournament_data,
        "svg_data": svg_data,
        "opts": Torneo._meta,  # Pasar opts explícitamente para compatibilidad con breadcrumbs
        "app_label": "tournaments",  # Pasar app_label explícitamente
        "players": players
    })
    #if(tournament.modo_torneo == 'Round') : context.update(results_table)
    return TemplateResponse(request, 'admin/tournament_view.html', context)



def save_svg(request):
    if (request.method != 'POST'):
        return JsonResponse({'status': 'error', 'message':'metodo no permitido'}, status=405)
    body_unicode = request.body.decode('utf-8')
    try:
        data = json.loads(body_unicode)
    except:
        return JsonResponse({'error': 'No se pudo decodificar el JSON'}, status=400)   
    svg_data = data.get('svg_data')
    torneo_id = data.get('torneo_id')
    if not svg_data or torneo_id == 0:
        return JsonResponse({'status': 'error', 'message':'No se pudo encontrar la data o se entrego un id = 0'}, status=400)
    try:
        file_name= str(torneo_id) + '.svg'
        parent_dir = STATICFILES_DIRS[0]
        file_path = os.path.join(parent_dir,'svg_tournaments',file_name)
        with open(file_path,'w') as file:
            file.write(svg_data)
        
    except Exception as e:
        print(e)
        print("Algo sucedio mal, variables usadas:")
        print(f"torneo_id:{torneo_id}")
        print(f"svg Data:{svg_data}")
        return JsonResponse({'status': 'error', 'message':'Hubo un problema al intentar guardar el svg'}, status=400)
    return JsonResponse({'status': 'success', 'message': 'SVG guardado correctamente.'})

# Funcion que devuelve una lista de objetos player con los datos necesarios de todos los usuarios incritos al torneo que se pasa como 
# argumento (por el momento solo pasa el username pero si se ocupa algo mas se puede cambiar)
def get_registered_players(torneo):
    raw_users = torneo.usuarios_torneo.all()
    return [user.username for user in raw_users]
    
    