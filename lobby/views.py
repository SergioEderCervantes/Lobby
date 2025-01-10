from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from django.http import HttpResponseRedirect
from tournaments.models import Torneo
from lobby.models import Comment, Promocion
from django.db import models
from .services import send_whatsapp_message

def custom_404(request, exception):
    return render(request, 'error_404.html', status=404)

def home(request):

    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        # Validacion fea de la longitud de comentario, en el front debe de estar la validacion bonita
        if len(comentario) <=  100:
            comment = Comment.objects.create(comentario=comentario, usuario=request.user)
            comment.save()
            # Mensaje de Whats a Christian
            success_message = f"""
            Lobby Web aplication: Se acaba de escribir un comentario en nuestra pagina!!
El comentario esta a nombre de {request.user.username}
El comentario dice lo siguiente:
{comentario}
            """
            response = send_whatsapp_message(success_message, "524492580708")
            print(response)
        return HttpResponseRedirect('/')
    else:

        # Hora actual del servidor
        ahora = now()
        comments = Comment.objects.all()

        promociones = Promocion.objects.filter(
                models.Q(tiene_vigencia = False) |
                models.Q(vigencia__gte=ahora.date())
                )
        
        # Rango de tiempo permitido
        inicio_rango = ahora - timedelta(hours=5)  # 5 horas atrás
        fin_rango = ahora + timedelta(minutes=30)  # 30 minutos adelante
        
        # Proximo torneo
        proximo_torneo = Torneo.objects.filter(fecha__gte=ahora).order_by('fecha').first()
        num_players = proximo_torneo.cantidad_usuarios_inscritos() if proximo_torneo else None
        torneo_ejec = Torneo.objects.filter(fecha__range=(inicio_rango, fin_rango)).first()
        
        # Corazones
        usuario = request.user
        
        num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0 
        
        context = {
        'promociones': promociones, 
        'prox_torneo': proximo_torneo, 
        'num_players': num_players, 
        'comments': comments,
        'torneo_ejec': torneo_ejec,
        'num_torneos_inscritos': num_torneos_inscritos,
        }

        return render(request, 'index.html', context=context)


