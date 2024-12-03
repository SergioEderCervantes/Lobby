import os
import json
from settings import STATICFILES_DIRS
from .eliminacion_directa import crearMatch
from .round_robin import createRounds
# Funciones de ayuda para otras vistas


def cargar_svg(file_path):
    # Carga y devuelve el contenido de un archivo SVG.
    with open(file_path, 'r') as svg_file:
        return svg_file.read()

def manejar_post(tournament, parent_dir):
    
    # Maneja la creación de los matchups según el modo del torneo.
    # Devuelve el contenido del SVG y actualiza el torneo como definido.
    players = tournament.usuarios_inscritos()
    print(players)
    modo = tournament.modo_torneo
    file_path = None

    if modo == 'Direct':
        file_path = crearMatch(players, tournament.pk, parent_dir=parent_dir)
    elif modo == 'Round':
        file_path = createRounds(players, tournament.pk, parent_dir=parent_dir)
    
    print(f"File path generado: {file_path}")
    svg_data = cargar_svg(file_path)
    tournament.is_defined = True
    tournament.save()

    return svg_data

def gestionar_svg_torneo(request, tournament):
    # Gestiona el flujo principal para cargar o generar SVG de un torneo.

    parent_dir = STATICFILES_DIRS[0]
    
    if tournament.is_defined:
        file_name = f"{tournament.pk}.svg"
        file_path = os.path.join(parent_dir, 'svg_tournaments', file_name)
        return cargar_svg(file_path)

    elif request.method == "POST":
        return manejar_post(tournament, parent_dir)
    
    return None

# -----------------------Guardado de SVG ------------------------------------


def decode_request_body(request):
    # Decodifica el cuerpo del request y devuelve los datos en formato JSON.
    try:
        body_unicode = request.body.decode('utf-8')
        return json.loads(body_unicode)
    except json.JSONDecodeError:
        raise ValueError("No se pudo decodificar el JSON")

def validar_svg_data(data):
    # Valida que los datos necesarios para guardar el SVG estén presentes.
    svg_data = data.get('svg_data')
    torneo_id = data.get('torneo_id')
    if not svg_data or not torneo_id:
        raise ValueError("No se pudo encontrar la data o se entregó un id inválido")
    return svg_data, torneo_id

def guardar_svg(svg_data, torneo_id):
    # Guarda los datos SVG en un archivo correspondiente al torneo.
    file_name = f"{torneo_id}.svg"
    parent_dir = STATICFILES_DIRS[0]
    file_path = os.path.join(parent_dir, 'svg_tournaments', file_name)

    try:
        with open(file_path, 'w') as file:
            file.write(svg_data)
    except Exception as e:
        raise IOError(f"Hubo un problema al intentar guardar el archivo SVG: {e}")

    return file_path



def gestionar_guardado_svg(request):
    # Decodificar el cuerpo del request
    data = decode_request_body(request)

    # Validar la data recibida
    svg_data, torneo_id = validar_svg_data(data)

    # Guardar el archivo SVG
    guardar_svg(svg_data, torneo_id)