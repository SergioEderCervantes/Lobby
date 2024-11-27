from django.shortcuts import render
from django.http import JsonResponse
from .forms import ReservationForm  # Asegúrate de tener el formulario definido

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
