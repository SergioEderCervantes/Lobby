from django.shortcuts import render
from django.http import JsonResponse
from users.models import User
import re

def update_profile(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método inválido"}, status=405)       
    
    
    try:
        usuario=request.user
        
        username = request.POST.get('username', usuario.username)
        email = request.POST.get('email', usuario.email)
        telefono = request.POST.get('telefono', usuario.telefono)
        avatar = request.FILES.get('avatar', usuario.avatar)  
        print(telefono)
        print(avatar)
        if not telefono.isdigit():
            return JsonResponse({'error': 'El número de teléfono debe ser válido'}, status=400)
        
        if '@' not in email or '.' not in email:
            return JsonResponse({'error': 'Por favor ingresa un correo electrónico válido.'}, status=400)
        if not re.match(r'^[a-zA-Z0-9._]+$', username):
            return JsonResponse({'error': 'Por favor ingresa un nombre de usuario válido.'}, status=400)

        usuario.username = username
        usuario.email = email
        usuario.telefono = telefono
        usuario.avatar = avatar
        usuario.save()
    
        return JsonResponse({'message': 'Jugador registrado como invitado correctamente'}, status=201)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
    
# Create your views here.
def custom_perfil(request):
    return render(request, 'custom_perfil.html', {})