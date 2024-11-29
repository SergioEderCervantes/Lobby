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
        
        # 1. Traer todos los datos del usuario con id 1
        cursor.execute("select id, first_name, last_name, username, email from users_user where id = 1")
        user = cursor.fetchall()

        # 2. Traer todos los torneos
        cursor.execute("SELECT id, nombre_juego, fecha, is_defined FROM tournaments_torneo")
        torneos = cursor.fetchall()

        # 3. Traer el nombre y apellido de todos los participantes de un torneo
        id_torneo = 1  # Ajusta el ID del torneo según sea necesario
        cursor.execute("""
            SELECT u.first_name, u.last_name 
            FROM tournaments_torneo_usuario ut
            JOIN users_user u ON u.id = ut.id
            WHERE ut.torneo_id = %s
        """, [id_torneo])
        participantes = cursor.fetchall()

        # 4. Obtener los usuarios que han realizado una reservación
        cursor.execute("""
            SELECT u.first_name, u.last_name 
            FROM users_user u
            JOIN reservations_reservacion r ON u.id = r.id
        """)
        usuarios_con_reservacion = cursor.fetchall()

        # 5. Obtener las promociones asociadas a la sucursal 1
        cursor.execute("""
            SELECT p.descripcion 
            FROM lobby_sucursal_promocion sp
            JOIN lobby_promocion p ON sp.promocion_id = p.id
            WHERE sp.sucursal_id = 1
        """)
        promociones_sucursal_2 = cursor.fetchall()

        # 6. Obtener todos los productos que pertenecen a la sucursal 3
        cursor.execute("""
            SELECT rp.nombre_producto 
            FROM lobby_sucursal_producto sp
            JOIN restaurante_producto rp ON sp.producto_id = rp.id
            WHERE sp.sucursal_id = 3
        """)
        productos_sucursal_3 = cursor.fetchall()

        # 7. Obtener todas las reservaciones del día 24/11/24
        cursor.execute("""
            SELECT * 
            FROM reservations_reservacion 
            WHERE fecha = '2024-11-24'
        """)
        reservaciones_24_nov = cursor.fetchall()

        # 8. Obtener todos los productos de tipo "bebidas_sin_alcohol"
        cursor.execute("""
            SELECT * 
            FROM restaurante_producto 
            WHERE tipo_producto = 'Bebidas_sin_alcohol'
        """)
        productos_bebidas_sin_alcohol = cursor.fetchall()

        # 9. Obtener todos los torneos del día 30/11/24
        cursor.execute("""
            SELECT * 
            FROM tournaments_torneo 
            WHERE fecha = '2024-11-30'
        """)
        torneos_30_nov = cursor.fetchall()

        # 10. Obtener la descripción de la promoción con id = 27
        cursor.execute("""
            SELECT descripcion 
            FROM lobby_promocion 
            WHERE id = 27
        """)
        promocion_27 = cursor.fetchall()

        # 11. Contar el número de reservaciones por sucursal, solo para las sucursales con más de 5 reservaciones
        cursor.execute("""
            SELECT s.nombre_sucursal, COUNT(r.id) AS total_reservaciones
            FROM reservations_reservacion r
            JOIN lobby_sucursal s ON r.sucursal_id = s.id
            GROUP BY s.nombre_sucursal
            HAVING COUNT(r.id) > 5
        """)
        sucursales_con_muchas_reservaciones = cursor.fetchall()
        
        # 12. Obtener la cantidad de productos por tipo, solo para los tipos con más de 10 productos
        cursor.execute("""
            SELECT p.tipo_producto, COUNT(sp.producto_id) AS total_productos
            FROM lobby_sucursal_producto sp
            JOIN restaurante_producto p ON sp.producto_id = p.id
            GROUP BY p.tipo_producto
            HAVING COUNT(sp.producto_id) > 10
        """)
        tipos_con_muchos_productos = cursor.fetchall()
        
        # 13. Contar el número de torneos por modo de torneo, solo los modos con más de 2 torneos
        cursor.execute("""
            SELECT t.modo_torneo, COUNT(t.id) AS total_torneos
            FROM tournaments_torneo t
            GROUP BY t.modo_torneo
            HAVING COUNT(t.id) > 2
        """)
        modos_con_muchos_torneos = cursor.fetchall()
        
        # 14. Obtener el número de usuarios inscritos por torneo, solo aquellos torneos con más de 3 usuarios inscritos
        cursor.execute("""
            SELECT t.nombre_torneo, COUNT(tu.usuario_id) AS total_usuarios
            FROM tournaments_torneo_usuario tu
            JOIN tournaments_torneo t ON tu.torneo_id = t.id
            GROUP BY t.nombre_torneo
            HAVING COUNT(tu.usuario_id) > 3
        """)
        torneos_con_muchos_usuarios = cursor.fetchall()
        
        # 15. Contar el número de reservaciones por fecha, solo para fechas con más de 10 reservaciones
        cursor.execute("""
            SELECT r.fecha_reservacion, COUNT(r.id) AS total_reservaciones
            FROM reservations_reservacion r
            GROUP BY r.fecha_reservacion
            HAVING COUNT(r.id) > 10
        """)
        fechas_con_muchas_reservaciones = cursor.fetchall()
        
        # 16. Obtener las promociones asociadas a la sucursal 1, solo las sucursales con más de 1 promoción
        cursor.execute("""
            SELECT s.nombre_sucursal, COUNT(sp.promocion_id) AS total_promociones
            FROM lobby_sucursal_promocion sp
            JOIN lobby_sucursal s ON sp.sucursal_id = s.id
            GROUP BY s.nombre_sucursal
            HAVING COUNT(sp.promocion_id) > 1
        """)
        sucursales_con_muchas_promociones = cursor.fetchall()
        
        # 17. Obtener todos los productos que pertenecen a la sucursal 3, solo si tienen más de 5 productos
        cursor.execute("""
            SELECT s.nombre_sucursal, COUNT(sp.producto_id) AS total_productos
            FROM lobby_sucursal_producto sp
            JOIN lobby_sucursal s ON sp.sucursal_id = s.id
            GROUP BY s.nombre_sucursal
            HAVING COUNT(sp.producto_id) > 5
        """)
        sucursales_con_muchos_productos = cursor.fetchall()
        
        # 18. Contar el número de productos por tipo y sucursal, solo los tipos que tienen más de 5 productos en una sucursal
        cursor.execute("""
            SELECT s.nombre_sucursal, p.tipo_producto, COUNT(sp.producto_id) AS total_productos
            FROM lobby_sucursal_producto sp
            JOIN restaurante_producto p ON sp.producto_id = p.id
            JOIN lobby_sucursal s ON sp.sucursal_id = s.id
            GROUP BY s.nombre_sucursal, p.tipo_producto
            HAVING COUNT(sp.producto_id) > 5
        """)
        productos_por_tipo_y_sucursal = cursor.fetchall()
        
        # 19. Contar el número de torneos por modo de torneo, solo los torneos que se realicen el 30 de noviembre
        cursor.execute("""
            SELECT t.modo_torneo, COUNT(t.id) AS total_torneos
            FROM tournaments_torneo t
            WHERE t.fecha = '2024-11-30'
            GROUP BY t.modo_torneo
            HAVING COUNT(t.id) > 0
        """)
        torneos_30_nov_por_modo = cursor.fetchall()

        
        # 20. Obtener el promedio de productos por sucursal, solo para aquellas sucursales que tengan más de 3 productos
        cursor.execute("""
            SELECT s.nombre_sucursal, AVG(sp.producto_id) AS promedio_productos
            FROM lobby_sucursal_producto sp
            JOIN lobby_sucursal s ON sp.sucursal_id = s.id
            GROUP BY s.nombre_sucursal
            HAVING COUNT(sp.producto_id) > 3
        """)
        promedio_productos_por_sucursal = cursor.fetchall()



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
        'sucursales_con_muchas_reservaciones': sucursales_con_muchas_reservaciones,
        'tipos_con_muchos_productos': tipos_con_muchos_productos,
        'modos_con_muchos_torneos': modos_con_muchos_torneos,
        'torneos_con_muchos_usuarios': torneos_con_muchos_usuarios,
        'fechas_con_muchas_reservaciones': fechas_con_muchas_reservaciones,
        'sucursales_con_muchas_promociones': sucursales_con_muchas_promociones,
        'sucursales_con_muchos_productos': sucursales_con_muchos_productos,
        'productos_por_tipo_y_sucursal': productos_por_tipo_y_sucursal,
        'torneos_30_nov_por_modo': torneos_30_nov_por_modo,
        'promedio_productos_por_sucursal': promedio_productos_por_sucursal,

    })

