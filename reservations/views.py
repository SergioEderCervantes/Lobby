import json
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ReservationForm  # Asegúrate de tener el formulario definido
from lobby.models import Sucursal
from .models import Consola, Consola_disponibilidad
from users.models import User
from .services import validar_fecha, validar_hora, crear_reserva

def reservations(request):
    if request.method == 'POST':
        
        form = ReservationForm(request.POST)

        if form.is_valid():
            # Procesar la reservación (puedes guardarlo en la base de datos si es necesario)
            #form.save()

            # Recopilar los datos de la reservación para pasarlos al frontend
            reservation_data = {
                'nombre': form.cleaned_data['nombre'],
                'email': form.cleaned_data['email'],
                'telefono': form.cleaned_data['telefono'],
                'fecha': form.cleaned_data['fecha'],
                'hora': form.cleaned_data['hora'],
                'num_personas': form.cleaned_data['num_personas'],
                'comentarios': form.cleaned_data['comentarios']
            }

            # Devolver los datos como JSON si estás usando AJAX
            #return JsonResponse({'success': True, 'data': reservation_data})
        else:
            return JsonResponse({'success': False, 'error': 'Formulario inválido'})

    else:
        form = ReservationForm()  # Crear el formulario vacío
    return render(request, 'reservations.html', {'form': form})


def check_availability(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
    
    data = json.loads(request.body)
    fecha_str = data.get('fecha')
    sucursal_id = data.get('sucursal_id')
    
    # Validacion de existencia de datos
    if not fecha_str or not sucursal_id:
        return JsonResponse({'error': 'Fecha y sucursal son requeridos.'}, status = 400)
    
    try:
        # Validacion fecha
        fecha = validar_fecha(fecha_str)
        
        # Validacion de sucursal 
        sucursal = Sucursal.objects.get(id = sucursal_id)
        
    except Sucursal.DoesNotExist:
        return JsonResponse({'error': 'Sucursal no encontrada'})
    except ValueError:
        return JsonResponse({'error': 'La fecha proporcionada no es valida'}, status = 400)
    except Exception as e:
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
        return JsonResponse({"error": "Metodo invalido"})
    try:
        
        data = json.loads(request.body)
        # Obtener los datos del body
        usuario_id = data.get('usuario_id')
        sucursal_id = data.get('sucursal_id')
        consola_id = data.get('consola_id')
        fecha_str = data.get('fecha')
        hora_str = data.get('hora')
        num_personas = data.get('num_personas')
        comentarios = data.get('comentarios', '')
        
        if not all([usuario_id,sucursal_id,fecha_str,hora_str,num_personas]):
            raise Exception("Todos los campos son requeridos")
        
        fecha = validar_fecha(fecha_str)
                
        # Verificar que la hora esté en formato adecuado
        hora = validar_hora(hora_str)
        # Validar que el número de personas sea mayor a 6
        if num_personas < 6:
            raise Exception("El número de personas debe ser mayor a 6.")
        
        # Verificar que la sucursal y la consola existan
        sucursal = Sucursal.objects.get(id=sucursal_id)


        try:
            consola = Consola.objects.get(id=consola_id)
        except Consola.DoesNotExist:
            consola = None

        # Obtener el usuario desde el ID
        usuario = User.objects.get(id=usuario_id)
       
        # Llamar a la función para crear la reserva
        reserva = crear_reserva(usuario, sucursal_id, consola_id, fecha, hora, num_personas, comentarios)
        
        # Responder con la reserva creada (puedes retornar más detalles si lo deseas)
        return JsonResponse({'message': 'Reserva creada exitosamente', 'reserva_id': reserva.id}, status=201)

    except Sucursal.DoesNotExist as e:
        return JsonResponse({'error': 'Error con la Sucursal '}, status=400)
    except User.DoesNotExist as e:
        return JsonResponse({'error': 'Error, con el usuario '}, status = 400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    