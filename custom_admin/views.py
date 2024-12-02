from tournaments.models import Torneo
from django.shortcuts import get_object_or_404  
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.db.models import Count
from .services import gestionar_svg_torneo, gestionar_guardado_svg
from django.http import HttpResponseNotFound
# Create your views here.

class Tournament(object):
    def __init__(self, name, game_name, mode, date, description, rules):
        self.name = name
        self.game_name = game_name
        self.mode = mode
        self.date = date
        self.description = description
        self.rules = rules
        # self.registered_players = registered_players
        # self.imagen = imagen



def tournament_view(request, tournament_id):
    # Dios perdoname
    from custom_admin.admin import admin_site
        
    # Obtener el torneo y su número de jugadores inscritos
    tournament = get_object_or_404(Torneo, id=tournament_id)

    # Obtener el número de jugadores inscritos
    num_players = tournament.cantidad_usuarios_inscritos()
    
    if not tournament.imagen:
        tournament.imagen = "https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png"
        tournament.save()

    # Obtener o crear el svg de los torneos si es que hace falta
    try:
        svg_data = gestionar_svg_torneo(request, tournament)
    except FileNotFoundError:
        return HttpResponseNotFound("El archivo SVG no existe.")

        
    # Obtener el contexto de custom_admin_site
    context = admin_site.each_context(request)
    
    # Extraer manualmente el app_label y otros detalles
    context.update({
        "title": f"Vista del Torneo: {tournament.nombre_torneo}",
        "torneo": tournament,
        "num_players": num_players,
        "svg_data": svg_data,
        "opts": Torneo._meta,  # Pasar opts explícitamente para compatibilidad con breadcrumbs
        "app_label": "tournaments",  # Pasar app_label explícitamente
    })
    return TemplateResponse(request, 'admin/tournament_view.html', context)



def save_svg(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

    try:
        gestionar_guardado_svg(request)

    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    except IOError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'Error inesperado: ' + str(e)}, status=500)

    return JsonResponse({'status': 'success', 'message': 'SVG guardado correctamente.'})
