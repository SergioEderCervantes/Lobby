import os
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.db import models
from django.db.models import Count, F, ExpressionWrapper
from django.http import JsonResponse
from django.db import IntegrityError
from django.utils.timezone import now
from datetime import date
from .models import Torneo
from users.models import User
from settings import STATICFILES_DIRS 

# Create your views here.

def tournaments(request):
    # Corazones 
    usuario = request.user
    
    num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0 
    
    hoy = date.today()
    tournaments = (
    Torneo.objects.filter(fecha__gte=hoy)
    .annotate(num_players=Count('jugadores_inscritos'))
    .annotate(days_to_today=ExpressionWrapper(F('fecha') - hoy, output_field=models.DurationField()))
    .order_by('days_to_today')  # Orden ascendente por días
)
    proximo_torneo = Torneo.objects.filter(fecha__gte=now()).order_by('fecha').first()    

    return render(request, 'tournaments.html', {'tournaments': tournaments, 'prox_torneo': proximo_torneo, 'num_torneos_inscritos': num_torneos_inscritos})


def tournament_detail(request, name):
        # Corazones 
    usuario = request.user
    
    num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0     
    
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
        'players': players,
        'num_torneos_inscritos': num_torneos_inscritos
    }


    return render(request, 'tournament_detail.html',context)


def register_player(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método inválido"}, status=405)
    
    try:
        data = json.loads(request.body)
        usuario_id = data.get('usuario_id')
        torneo_id = data.get('torneo_id')
        # Validar existencia
        if not torneo_id or not usuario_id:
            raise Exception("No se pudieron conseguir los datos del body")
        # Obtener objetos user y torneos
        usuario = User.objects.get(id = usuario_id)
        torneo = Torneo.objects.get(id = torneo_id)
        
        # Verificar si el usuario ya está inscrito
        if torneo.jugadores_inscritos.filter(id=usuario.id).exists():
            return JsonResponse({'message': 'El usuario ya está inscrito en este torneo.'}, status=200)

        # Inscribir al usuario en el torneo
        torneo.jugadores_inscritos.add(usuario)
        
        # Actualizar su numero de torneos inscritos y mandar mensaje si es que tiene la promocion
        mensaje = 'Felicidades!! su inscripcion a este torneo es gratuita!!.' if usuario.agregar_juego(torneo.nombre_juego) else 'Usuario inscrito exitosamente al torneo.' 


        return JsonResponse({'message': mensaje}, status=201)

        
    except (User.DoesNotExist, Torneo.DoesNotExist) as e:
        return JsonResponse({'error': f'{e.model.__name__} no encontrada'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
    
def register_guest_player(request, torneo_id):
    if request.method != "POST":
        return JsonResponse({"error": "Método inválido"}, status=405)
    
    try:
        # Obtener datos del formulario
        player_name = request.POST.get("playerName")
        telefono = request.POST.get("tel")

        # Validar que los campos requeridos no estén vacíos
        if not player_name or not telefono:
            return JsonResponse({'error': 'Todos los campos son requeridos'}, status=400)

        # Validar que el teléfono sea numérico
        if not telefono.isdigit():
            return JsonResponse({'error': 'El número de teléfono debe ser válido'}, status=400)

        # Crear el usuario con el tipo "Guest"
        user = User.objects.create_user(
            username=player_name,  # El nombre del jugador será el username
            password=None,  # Sin contraseña porque es invitado
            tipo_usuario = 'GU',
            telefono = telefono
        )
        # Asociar el usuario al torneo
        torneo = Torneo.objects.get(id=torneo_id)
        torneo.jugadores_inscritos.add(user)

        return JsonResponse({'message': 'Jugador registrado como invitado correctamente'}, status=201)
    except IntegrityError as e:
        return JsonResponse({"error:": f"Error de integridad: {str(e)}"}, status=500)
    except ValueError as e:
        return JsonResponse({'error': f'Error en los valores provistos {str(e)}'}, status=500)
    except TypeError as e:
        return JsonResponse({'error': f'Errpr de tipo: {str(e)}'}, status=500)
    except Torneo.DoesNotExist:
        return JsonResponse({'error': 'El torneo no existe'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)
    