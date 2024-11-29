from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.db import connection


class Promocion(object):
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen
def home(request):
    promociones = {
        
            Promocion( "promocion1", static('img/promo.png')),
            Promocion( "promocion2", static('img/promo.png')),
            Promocion( "promocion3", static('img/promo.png')),
            Promocion( "promocion4", static('img/promo.png')),
            Promocion( "promocion5", static('img/promo.png')),
            Promocion( "promocion6", static('img/promo.png')),
        
    }
    return render(request, 'index.html', {'promociones' : promociones})

from django.db import connection
from django.shortcuts import render

def sql(request):
    # Consultas SQL
    with connection.cursor() as cursor:
        
        # 1. Traer todos los datos del usuario con id 3
        cursor.execute("select id, first_name, last_name, username, email from users_user where id = 1")
        user = cursor.fetchall()

        # 2. Traer todos los torneos
        cursor.execute("SELECT id, nombre_juego, fecha, is_defined FROM torneo")
        torneos = cursor.fetchall()

        # 3. Traer el nombre y apellido de todos los participantes de un torneo
        id_torneo = 1  # Ajusta el ID del torneo según sea necesario
        cursor.execute("""
            SELECT u.first_name, u.last_name 
            FROM torneo_usuarios_torneo ut
            JOIN users_user u ON u.id = ut.id
            WHERE ut.id_torneo = %s
        """, [id_torneo])
        participantes = cursor.fetchall()

        # 4. Obtener los usuarios que han realizado una reservación
        cursor.execute("""
            SELECT u.nombre, u.apellido 
            FROM users_user u
            JOIN reservaciones r ON u.id = r.id
        """)
        usuarios_con_reservacion = cursor.fetchall()

        # 5. Obtener las promociones asociadas a la sucursal 2
        cursor.execute("""
            SELECT p.descripcion 
            FROM sucursal_promocion sp
            JOIN promociones p ON sp.id_promocion = p.id_promocion
            WHERE sp.id_sucursal = 2
        """)
        promociones_sucursal_2 = cursor.fetchall()

        # 6. Obtener todos los productos que pertenecen a la sucursal 3
        cursor.execute("""
            SELECT p.nombre 
            FROM sucursal_producto sp
            JOIN productos p ON sp.id_producto = p.id_producto
            WHERE sp.id_sucursal = 3
        """)
        productos_sucursal_3 = cursor.fetchall()

        # 7. Obtener todas las reservaciones del día 24/11/24
        cursor.execute("""
            SELECT * 
            FROM reservaciones 
            WHERE fecha = '2024-11-24'
        """)
        reservaciones_24_nov = cursor.fetchall()

        # 8. Obtener todos los productos de tipo "bebidas_sin_alcohol"
        cursor.execute("""
            SELECT * 
            FROM productos 
            WHERE tipo = 'Bebidas_sin_alcohol'
        """)
        productos_bebidas_sin_alcohol = cursor.fetchall()

        # 9. Obtener todos los torneos del día 30/11/24
        cursor.execute("""
            SELECT * 
            FROM torneos 
            WHERE fecha = '2024-11-30'
        """)
        torneos_30_nov = cursor.fetchall()

        # 10. Obtener la descripción de la promoción con id = 27
        cursor.execute("""
            SELECT descripcion 
            FROM promociones 
            WHERE id_promocion = 27
        """)
        promocion_27 = cursor.fetchall()



    # Renderizar los resultados de todas las consultas
    return render(request, 'sql.html', {
        'user': user,
        'torneos': torneos,
        'participantes': participantes,
        'usuarios_con_reservacion': usuarios_con_reservacion,
        'promociones_sucursal_2': promociones_sucursal_2,
        'productos_sucursal_3': productos_sucursal_3,
        'reservaciones_24_nov': reservaciones_24_nov,
        'productos_bebidas_sin_alcohol': productos_bebidas_sin_alcohol,
        'torneos_30_nov': torneos_30_nov,
        'promocion_27': promocion_27,
    })

