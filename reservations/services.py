from datetime import date, timedelta, datetime, time
from django.db import transaction
from lobby.models import Sucursal
from .models import Consola, Consola_disponibilidad, Reservation


# Validacion de fecha (minimo un dia de anticipacion, maximo 30 dias)
# Convertir fecha a objeto datetime.date y hacer validaciones de un rango permitido 
def validar_fecha(fecha):
    # Verificar si el tipo de la fecha es un string
    if isinstance(fecha, str):
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
    # Verificar si la fecha es un objeto datetime o date
    elif not isinstance(fecha, (datetime, datetime.date)):
        raise TypeError("La fecha debe ser de tipo 'str', 'datetime' o 'date'.")

    hoy = date.today()
    fecha_minima = hoy + timedelta(days=1)
    fecha_maxima = hoy + timedelta(days=30)
    
    if fecha < fecha_minima:
        raise ValueError("La fecha debe ser al menos un día después de la fecha actual.")
    if fecha > fecha_maxima:
        raise ValueError("La fecha debe ser dentro del mes siguiente a la fecha actual.")
    return fecha
    
    
# Funcion que valida el formato de la hora y si esta dentro del rango permitido (por el momento de las 
# 16:00 a las 23:00 pero puede cambiar)
def validar_hora(hora):
    # Si la hora es una cadena, intentar convertirla a un objeto datetime
    if isinstance(hora, str):
        hora = datetime.strptime(hora, '%H:%M').time()  # Convertir string 'HH:MM' a objeto time

    
    # Verificar si la hora es un objeto datetime.time
    elif not isinstance(hora, time):
        raise TypeError("La hora debe ser de tipo 'str' o 'time'.")

    # Definir el rango de horas válidas (4:00 PM - 11:00 PM)
    hora_inicio = time(16, 0)  # 4:00 PM
    hora_fin = time(23, 0)     # 11:00 PM

    # Verificar si la hora está dentro del rango permitido
    if not (hora_inicio <= hora <= hora_fin):
        raise ValueError("La hora debe estar entre las 16:00 y las 23:00.")

    return hora


# Crear la disponibilidad del dia de hoy en un mes
def inicializar_disponibilidad(fecha_objetivo):
    # hoy = date.today()
    # fecha_objetivo = hoy + timedelta(days=30)
    sucursales = Sucursal.objects.all()
    consolas = Consola.objects.all()
    
    for sucursal in sucursales:
        for consola in consolas:
            Consola_disponibilidad.objects.get_or_create(
                consola = consola,
                sucursal = sucursal,
                fecha = fecha_objetivo,
                defaults={'disponibles': consola.disponibilidad_diaria}
            )

# Borrar la informacion de disponibilidad del dia de antier (cambiar a gusto)
def borrar_disponibilidad():
    hoy = date.today()
    fecha_objetivo = hoy - timedelta(days=2)
    
    disponibilidad_objetivo = Consola_disponibilidad.objects.filter(fecha=fecha_objetivo)
    
    if disponibilidad_objetivo:
        disponibilidad_objetivo.delete()
        

# Funcion que toma todos los datos, aunque ya se hayan validado hace unas ultimas validaciones y crea la 
# Reservacion con todos los datos
def crear_reserva(usuario, sucursal_id, consola_id, fecha, hora, num_personas, comentarios):
    with transaction.atomic():
        # Obtener la disponibilidad de la consola
        disponibilidad = Consola_disponibilidad.objects.select_for_update().get(
            sucursal_id=sucursal_id, consola_id=consola_id, fecha=fecha
        )
        
        # Validar si hay consolas disponibles
        if disponibilidad.disponibles <= 0:
            raise ValueError("No hay consolas disponibles para esta fecha.")
        
        # Decrementar disponibilidad
        disponibilidad.disponibles -= 1
        disponibilidad.save()

        # Crear la reserva
        Reservation.objects.create(
            username=usuario,  
            email=usuario.email,  
            sucursal_id=sucursal_id,  
            consola_seleccionada_id=consola_id,  
            fecha=fecha,  
            fecha_reservacion=fecha,  
            hora=hora,  
            num_personas=num_personas,  
            comentarios=comentarios  
        )
        return True  


# Funcion que crea la disponibilidad diara de los siguientes 30 dias (only test)
def init_disponibilidad():
    hoy = date.today()
    for i in range(60):
        inicializar_disponibilidad(hoy + timedelta(days=i))
