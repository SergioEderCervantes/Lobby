from django.shortcuts import render
from tournaments.models import Tournament_prueba, Users_prueba
from custom_admin.services import crearMatch
from django.shortcuts import get_object_or_404  
import os
import json
from django.http import JsonResponse
from settings import STATICFILES_DIRS
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


def save_svg(request):
    if (request.method != 'POST'):
        return JsonResponse({'status': 'error', 'message':'metodo no permitido'}, status=405)
    data = json.loads(request.body.decode('utf-8'))
    svg_data = data.get('svg_data')
    torneo_id = data.get('torneo_id')
    
    if not svg_data or torneo_id == 0:
        return JsonResponse({'status': 'error', 'message':'No se pudo encontrar la data o se entrego un id = 0'}, status=400)
    try:
        file_name= str(torneo_id) + '.svg'
        file_path = os.path.join(STATICFILES_DIRS,'svg',file_name)
        with open(file_path,'w') as file:
            file.write(svg_data)
    except:
        print("Algo sucedio mal, variables usadas:")
        print(f"torneo_id:{torneo_id}")
        print(f"svg Data:{svg_data}")
        print(f"file path: {file_path}")
        return JsonResponse({'status': 'error', 'message':'Hubo un problema al intentar guardar el svg'}, status=400)
    return JsonResponse({'status': 'success', 'message': 'SVG guardado correctamente.'})

        




    #     if svg_data:
    #         # Define la ruta y el nombre del archivo
    #         file_path = os.path.join('ruta/donde/quieras/guardar', 'archivo.svg')
    #         with open(file_path, 'w') as file:
    #             file.write(svg_data)  # Guarda el SVG

    #         return JsonResponse({'success': True})

    # return JsonResponse({'success': False}, status=400)

#     from django.urls import path
# from .views import guardar_svg

# urlpatterns = [
#     path('guardar-svg/', guardar_svg, name='guardar_svg'),
# ]-