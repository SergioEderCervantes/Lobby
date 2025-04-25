import json
import random
from django.shortcuts import render
from django.http import JsonResponse
from lobby.models import Sucursal
from .models import Consola, Consola_disponibilidad
from users.models import User
from .services import validar_fecha, validar_hora, crear_reserva
from lobby.services import notify
from django.templatetags.static import static

def reservations(request):
        # Corazones 
    usuario = request.user
    
    num_torneos_inscritos = usuario.num_torneos_dif_inscritos() if usuario.is_authenticated else 0 
    
    
    
    # Fondo cambiante 
    match random.randint(1,4):
        case 1:
            imagen_fondo = static("img/BG-XBOX.jpg")
        case 2:
            imagen_fondo = static("img/BG-PLAY.jpg")
        case 3:
            imagen_fondo = static("img/BG-NINTENDO1.webp")
        case 4:
            imagen_fondo = static("img/BG-BILLAR.jpeg")

    
    return render(request, 'reservations.html', {'num_torneos_inscritos': num_torneos_inscritos, 'background': imagen_fondo})

def check_availability(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
    
    try:
        data = json.loads(request.body)
        fecha_str = data.get('fecha')
        sucursal_id = data.get('sucursal_id')
        
        # Validacion de existencia de datos
        if not fecha_str or not sucursal_id:
            return JsonResponse({'error': 'Fecha y sucursal son requeridos.'}, status = 400)

        # Validacion fecha
        print(fecha_str)
        fecha = validar_fecha(fecha_str)
        
        # Validacion de sucursal 
        sucursal = Sucursal.objects.get(id = sucursal_id)
        
    except Sucursal.DoesNotExist:
        print("SUCURSAL") 
        return JsonResponse({'error': 'Sucursal no encontrada'})
    except ValueError as e:
        print("VALUE") 
        print(str(e))
        return JsonResponse({'error': 'La fecha proporcionada no es valida'}, status = 400)
    except Exception as e:
        print("GENERAL: " + str(e)) 
        return JsonResponse({'error': e}, status = 400)
    
    
    # Consultar disponibilidad
    disponibilidades = Consola_disponibilidad.objects.filter(sucursal=sucursal, fecha=fecha)
    resultado = {
        disponibilidad.consola.nombre: disponibilidad.disponibles
        for disponibilidad in disponibilidades
    }
    return JsonResponse({'disponibilidad': resultado}, status= 200)

def register_reservation(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método inválido"}, status=405)
    
    try:
        # Obtener los datos del body
       
        data = request.POST
        usuario = request.user
        sucursal_id = data.get('sucursal_id')
        consola_name = data.get('consola_name')
        fecha_str = data.get('fecha')
        hora_str = data.get('hora')
        num_personas = data.get('num_personas')
        comentarios = data.get('comentarios', '')
        # Validar que todos los campos requeridos estén presentes
        if not all([usuario, sucursal_id, consola_name, fecha_str, hora_str, num_personas]):
            raise ValueError("Todos los campos son requeridos")

        # Validar fecha y hora
        fecha = validar_fecha(fecha_str)
        hora = validar_hora(hora_str)
        print(type(num_personas))
        # Validar el número de personas
        if int(num_personas) < 6:
            raise ValueError("El número de personas debe ser mayor a 6.")

        # Verificar que la sucursal, consola y usuario existan
        sucursal = Sucursal.objects.get(id=sucursal_id)
        consola = Consola.objects.get(nombre=consola_name) if (consola_name != "sin-consola") else None

        # Llamar a la función para crear la reserva
        reserva_creada = crear_reserva(usuario, sucursal_id, consola.pk, fecha, hora, num_personas, comentarios)

        if reserva_creada:
            # Crear mensaje
            success_msg = f"""
            Se acaba de realizar una reservacion a nombre de: {usuario.username}!!!
Datos de la Reservacion:
    -Fecha y hora: {fecha}, {hora}
    -Numero de personas: {num_personas}
    -Consola elegida: {consola_name}
    -Comentarios adicionales: {comentarios}
    -Telefono de contacto: {usuario.telefono}
            """
            notify(success_msg)
            
            return JsonResponse({'message': 'Reservacion creada exitosamente'}, status=201)

        return JsonResponse({'error': 'No se pudo crear la reservacion'}, status=400)
    
    except (Sucursal.DoesNotExist, Consola.DoesNotExist, User.DoesNotExist) as e:
        return JsonResponse({'error': f'{e.model.__name__} no encontrada'}, status=400)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Ocurrió un error inesperado: {str(e)}'}, status=400)
