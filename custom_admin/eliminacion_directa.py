import random
import math
from collections import deque
import svgwrite
import os
# from settings import STATICFILES_DIRS


class Match:
    def __init__(self,id,player1,player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2



def print_ideal(matches, label):
    print(label)
    for match in matches:
        print(f"[{match.id}]: {match.player1} vs {match.player2}")

def print_no_ideal(matches, label):
    
    # print("Enfrentamientos adicionales:")   
    # for adicional in adicionales:
    #     print(f"[{adicional.id}]: {adicional.player1} vs {adicional.player2}")
    print(label) 
    for match in matches:
        print(f"[{match.id}]: {match.player1} vs {match.player2}")


# Creacion de emparejamiento cuando el numero de jugadores es potencia de dos
def emparejamiento_ideal(matches, jugadores, n, iterador_id):
    for i in range(0,n,2):
        matches.append(
            Match(str(next(iterador_id)),jugadores[i], jugadores[i+1])
        )
    print_ideal(matches, "hola")



    
# Creacion de emparejamiento cuando el numero de jugadores NO es potencia de dos
def emparejamiento_no_ideal(matches,jugadores, n, iterador_id, adicionales):
    j = int(math.log2(n))
    res = n - 2**j
    adicionales = []
    jugadores_ptr = 0
    # Adicionales
    for jugadores_ptr in range(0, res*2, 2): 
        aux = Match(str(next(iterador_id)),jugadores[jugadores_ptr],jugadores[jugadores_ptr+1])
        # matches.append(aux)
        adicionales.append(aux)
    jugadores_ptr = jugadores_ptr + 2
    #se los matches del bracket principal, inicialmente vacios 
    bracket_principal = deque([Match('-', '-', '-') for _ in range(2**(j-1))]) 

    for match in adicionales:
        if bracket_principal[0].id == '-': #Primera vez que pasa este elemento por el ciclo
            bracket_principal[0].id = str(next(iterador_id))
            bracket_principal[0].player1 = match.id
        else:   # Ya se habia pasado este elemento por  el ciclo, ya tiene el player1
            bracket_principal[0].player2 = match.id
        bracket_principal.rotate(-1)

    # Terminar de llenar el bracket principal y copiarlos en la lista Matches
    for final_match in bracket_principal:
        if final_match.id == '-':   # El ciclo anterior no lo toco
            final_match.id = str(next(iterador_id))
            final_match.player1 = jugadores[jugadores_ptr]
            final_match.player2 = jugadores[jugadores_ptr + 1]
            jugadores_ptr = jugadores_ptr + 2
        elif final_match.player2 == '-':  # El ciclo anterior lo paso una vez, ya tiene id y player1
            final_match.player2 = jugadores[jugadores_ptr]
            jugadores_ptr = jugadores_ptr + 1
        # Para este punto, el match esta completo
        matches.append(final_match)
    
    return  organizar_matchups(matches, adicionales)


def crearMatch(jugadores = [], tournament_id = 0, parent_dir = ""):
    n = len(jugadores)
    matches = []
    adicionales = []
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return
    iterador_id = iter(range(1,65))
    random.shuffle(jugadores)
    is_ideal = False
    if (n & (n - 1)) == 0 :     #los jugadores inscritos son potencia perfecta de 2, matching tradicional
        emparejamiento_ideal(matches, jugadores, n, iterador_id)
        is_ideal = True
        print_ideal(matches, "hola")
    else:
        adicionales = emparejamiento_no_ideal(matches,jugadores,n, iterador_id, adicionales)
        #  juntar adicionales con matches, primero los adicionales, asi queda todo en un arreglo
        print_no_ideal(adicionales,"hola")
       

    file_path = create_svg_match(matches, adicionales, tournament_id, parent_dir, is_ideal, iterador_id)
    return file_path


# Funcion que toma el bracket principal y los adicionales y los organiza para ya estar listos para la creacion
# Del SVG, tambien agrega matchups de relleno para que quede mas acomodado
def organizar_matchups(matches = [], adicionales = []):
    nuevos_adicionales = []
    # Primero organizamos ek bracket principal por orden de numero
    matches.sort(key= lambda obj: int(obj.id))
    # Ahora organizar los adicionales para que coincidan con el bracket principal
    for match in matches:
        if not match.player1.isdigit():
            # El match no tiene adicionales, evalua al siguiente
            nuevos_adicionales.append(Match("-","-","-"))
            nuevos_adicionales.append(Match("-","-","-"))
            continue
        id_adicional = match.player1
        adicional = next((ad for ad in adicionales if ad.id == id_adicional), None)
        nuevos_adicionales.append(adicional)
        # Ya metido el primer adicional, comprobamos que el segundo sea adicional
        if match.player2.isdigit():
            # Hay otro adicional, hay que meterlo
            id_adicional = match.player2
            adicional = next((ad for ad in adicionales if ad.id == id_adicional), None)
            nuevos_adicionales.append(adicional)
        else:
            # No hay otro adicional, agregar un match vacio
            nuevos_adicionales.append(Match("-","-","-"))
            
    return nuevos_adicionales
            
    
# ------------------------------------------------------------ Creacion del SVG de los torneos -----------------------------------
# Toma como argumento un arreglo de objetos Match y un putero de cosas mas as olweis odio python
# Regresa el path donde se supone que se creo el svg
def create_svg_match(matchups, adicionales, tournament_id, parent_dir, is_ideal, iterador_id):

    dwg = svgwrite.Drawing()
    STAGES = ['Final', 'Semifinal', 'Cuartos', 'Octavos', '16th']
    
    # gupos para organizar los elementos
    machups_group = dwg.g(id="g__enfrentamientos")
    lines_group = dwg.g(id="g__conectores")
    LEVELS = int(math.log2(len(matchups))) + 1 
    XOFFSET = 250
    YOFFSET=100
    SCALE = 2

    
    # Arreglo de arreglos, cada posicion tendra un arreglo de match_squares, los cuales son un svg group
    connector_points = []
    cx = 150
    # Creacion de rectangulos de match
    if not is_ideal:
        # Primero llenas con los adicionales
        machups_group.add(dwg.rect(insert=(cx-75,30), size=(150,35), fill="#a1a1a1", rx=3, ry=3, class_="label__rect"))
        text = dwg.text("Adicionales",insert=(cx,50), class_="etiquetas_levels", font_weight = 700, fill="white")
        text.attribs["dominant-baseline"] = "middle"
        text.attribs["text-anchor"] = "middle"
        machups_group.add(text)
        aux = []
        cy = YOFFSET/2 + 100
        for adicional in adicionales:
            if adicional.id !="-":
                match_square = create_match_square(dwg, adicional, cx, cy)
                aux.append(match_square)
                machups_group.add(match_square)
            cy = cy + YOFFSET
        cx = cx + XOFFSET
        connector_points.append(aux)
    iterador_jugadores = iter(range(1, 64)) if is_ideal else iter(range(len(connector_points[0])+1, 64))
    # Ahora todo lo demas
    for level in range (LEVELS):
        aux = []
        cy = YOFFSET * math.pow(SCALE,level)/2 + 100 if is_ideal else YOFFSET * math.pow(SCALE,level+1)/2 + 100
        matches_in_level = int(len(matchups) / math.pow(SCALE,level))
        label = STAGES[LEVELS - level - 1]
        machups_group.add(dwg.rect(insert=(cx-75,30), size=(150,35), fill="#a1a1a1", rx=3, ry=3, class_="label__rect"))
        text = dwg.text(label,insert=(cx,50), class_="etiquetas_levels", font_weight = 700, fill="white")
        text.attribs["dominant-baseline"] = "middle"
        text.attribs["text-anchor"] = "middle"
        machups_group.add(text)

        for i in range(0,matches_in_level):
            match_data = matchups[i] if level == 0 else Match(str(next(iterador_id)),
                                                            str(next(iterador_jugadores)), str(next(iterador_jugadores)))
            match_square = create_match_square(dwg, match_data, cx, cy)
            aux.append(match_square)
            machups_group.add(match_square)
            cy = cy + YOFFSET * math.pow(SCALE,level) if is_ideal else cy + YOFFSET * math.pow(SCALE,level+1)
        cx = cx + XOFFSET
        connector_points.append(aux)

    # Creacion de lineas que conectan los match
    # Si el match no es ideal, el primer connect Levels va a mandar un False, despues ya todo lo demas es true, si es ideal siempre es True
    band = is_ideal
    for i in range(0, len(connector_points)):
        if i + 1 != len(connector_points):
            connect_levels(dwg, lines_group, band, connector_points[i], connector_points[i+1])  
        band = True
    
    # Guardar todos los elementos creados
    dwg.add(machups_group)
    dwg.add(lines_group)
    
    # Calcular las dimensiones que debe de tener el svg
    width, height = get_max_dimensions(dwg.elements)
    # Guardar el SVG creado 
    
    SVG_NAME = os.path.join(parent_dir,'svg_tournaments', str(tournament_id) + '.svg')
    
    id="svg_enfrentamientos"
    dwg['width'] = width + 200
    dwg['height'] = height + 200
    dwg['id'] = id
    dwg['viewBox'] = f"0 0 {width + 200} {height + 50}"
    dwg.saveas(filename=SVG_NAME,pretty=True)

    print(f"Width: {width}")
    print(f"Height: {height}")
    
    return SVG_NAME

    

# Crea los componentes graficos para un rectangulo de matchup con todos los datos que se le envian de parametros
# Regresa un grupo con todos los elementos
def create_match_square(dwg, match_data, cx, cy):
    MATCH_WIDTH = '200px'
    MATCH_HEIGHT = "50px"
    x = cx - 0.5 * 200
    y = cy - 0.5 * 50
    match_group = dwg.g(id="match__"+match_data.id, class_="matchup")
    
    # Rectangulo de fondo
    match_group.add(dwg.rect(insert=(x,y), size=(MATCH_WIDTH,MATCH_HEIGHT), fill = '#444444', rx=10, ry=10,class_="fondo_matchup"))
    # Rectangulo de id
    radius = 10
    width, height = 25, 50
    
    path_data = f"M {x + radius},{y} " \
            f"h {width - radius} " \
            f"v {height} " \
            f"h {-width + radius} " \
            f"a {radius},{radius} 0 0 1 {-radius},{-radius} " \
            f"v {-height + 2 * radius} " \
            f"a {radius},{radius} 0 0 1 {radius},{-radius} " \
            f"Z"
    
    match_group.add(dwg.path(d=path_data, fill="#a1a1a1", class_="matchup__id__container"))
    match_group.add(dwg.text(match_data.id, insert=(x+8, y+30), class_="matchup__id", font_weight = 700))
    # Rectangulo de los jugadores
    match_group.add(dwg.rect(insert=(x+25,y), size=('175px',MATCH_HEIGHT), rx=10, ry=10, fill='#444444', class_="players__container"))
    # Jugadores
    # Si es un rectangulo que no tiene jugadores, se referencia la clase como blanco
    className  ="matchup__player draggable" if not match_data.player1.isdigit() else "matchup__player"
    
    
    group1 = dwg.g(class_=className)
    group1.add(dwg.rect(insert=(x+25,y), size=('175px','25px'), fill='#444444',rx=10, ry=10))
    group1.add(dwg.text(match_data.player1, insert=(x+30, y+18), class_="matchup__player1", fill="white", font_size="14px"))
    match_group.add(group1)
    
    className  ="matchup__player draggable" if not match_data.player2.isdigit() else "matchup__player"
    group2 = dwg.g(class_=className)
    group2.add( dwg.rect(insert=(x+25,y+25), size=("175px","25px"), fill="#444444", rx=10, ry=10))
    group2.add(dwg.text(match_data.player2, insert=(x+30, y+45), class_="matchup__player2", fill="white", font_size="14px"))
    match_group.add(group2)
    

    # Campo para insersion del puntaje
    # match_group.add(dwg.rect(insert=(x+175,y), size=("25px", "25px"), fill='#a1a1a1', rx=10,ry=10, class_="match__puntaje__player1"))
    width, height = 25, 25
    path_data = f"M {x + 175},{y} " \
            f"h {width - radius} " \
            f"a {radius},{radius} 0 0 1 {radius},{radius} " \
            f"v {height - radius} " \
            f"h {-width} " \
            f"v {-height} " \
            f"Z"
                
    match_group.add(dwg.path(d=path_data, fill="#a1a1a1", class_="match__puntaje__player1"))
    match_group.add(dwg.text("", insert=(x+180, y + 17), class_='match__puntaje__player1__text', fill="black", font_size="14px", font_weight = 700))
    path_data = f"M {x + 175},{y + 25} " \
            f"h {width} " \
            f"v {height - radius} " \
            f"a {radius},{radius} 0 0 1 {-radius},{radius} " \
            f"h {-width + radius} " \
            f"v {-height} " \
            f"Z"
    match_group.add(dwg.path(d=path_data, fill="#a1a1a1", class_="match__puntaje__player2"))
    match_group.add(dwg.text("", insert=(x+180, y + 42), class_='match__puntaje__player2__text', fill="black", font_size="14px", font_weight = 700))
   
    # Linea entre los jugadores
    match_group.add(dwg.line(start=(x+25, y+25), end=(x+200, y+25),stroke="white", stroke_width=1, class_="divisor_line"))
    
    # Linea para diferenciar la parte de jugadores de la parte de la insersion de puntaje
    match_group.add(dwg.line(start=(x+175,y), end = (x+175,y+50), stroke="white", stroke_width=1, class_="divisor_line_2"))
    return match_group
    
# Funcion que, dado dos niveles del torneo, 
def connect_levels(dwg,group, is_ideal, level1, level2):
    pivot = 0
    if is_ideal:
        for match in level2:
            center1 = get_group_center(level1[pivot]) 
            point1 = (center1[0]+100, center1[1])
            
            
            center2 = get_group_center(level1[pivot+1]) 
            point2 = (center2[0]+100, center2[1])
            
            center3 = get_group_center(match)
            center_point= (center3[0] - 100, center3[1])
            
            group.add(dwg.polyline([point1,center_point],fill='none', stroke="white", stroke_width=2, class_="connective__lines"))
            group.add(dwg.polyline([point2,center_point],fill='none', stroke="white", stroke_width=2, class_="connective__lines"))
            pivot +=2
    else:
        for match in level1:
            # Sacamos el match target que se tiene que conectar el match
            match_id = get_group_id(match)
            match_id = match_id.split("__")[1]
            target = next((match_lvl_2 for match_lvl_2 in level2 if es_siguiente_match(match_id,match_lvl_2)), None)
            # Con match como inicio y Target como final, sacamos los centros y creamos la linea
            center1 = get_group_center(match)
            point1 = (center1[0] + 100, center1[1])
            target_center = get_group_center(target)
            target_point = (target_center[0] - 100, target_center[1])
            
            group.add(dwg.polyline([point1,target_point], fill='none', stroke="white", stroke_width=2, class_="connective__lines"))
            
            


# Funcion que ayuda a calcular el centro del rectangulo principal del fondo del grupo que se le pasa como argumento
# Regresa una tupla con el centro del grupo
def get_group_center(group):
    rect = group.elements[0]  # Accedemos al primer elemento del grupo (el rectángulo)
    x = rect['x']
    y = rect['y']
    width = rect['width']
    height = rect['height']
    
    # Convertir valores de cadena a enteros (si tienen "px", removerlo)
    x, y = int(x), int(y)
    width, height = int(width.replace("px", "")), int(height.replace("px", ""))
    
    # Calcular el centro
    cx = x + width / 2
    cy = y + height / 2
    return (cx, cy)

# Funcion que dado un elemento group devuelve el id relacionado
def get_group_id(group):
    return group.attribs.get("id")

# Funcion que dado un grupo, busca los grupos hijos que tengan la misma clase a la que se referencia y 
# devuelve un arreglo del texto que contiene cada grupo de la clase
def get_text_from_class(group, target_class = "matchup__player"):
    texts = []
    for element in group.elements:
        # Verificar si el elemento es un grupo con la clase target_class
        if isinstance(element, svgwrite.container.Group) and target_class in element.attribs.get("class", ""):
            # Buscar elementos de texto dentro de este subgrupo
            for sub_element in element.elements:
                if isinstance(sub_element, svgwrite.text.Text):
                    texts.append(sub_element.text)  # Agregar el texto al resultado
    return texts

# Funcion que valida si el objeto group target tiene como jugadores el match_id que es el id de un match de lvl inferior 
def es_siguiente_match(match_id, target):
    texts = get_text_from_class(target)
    for text in texts:
        if text == match_id: 
            return True
        
    return False

def get_max_dimensions(elements, max_x = 0, max_y = 0):
    """
    Recursivamente encuentra las coordenadas máximas de los elementos.
    """
    for element in elements:
        if isinstance(element, svgwrite.container.Group):  # Si es un grupo, iterar recursivamente
            max_x, max_y = get_max_dimensions(element.elements, max_x, max_y)
        else:
            attribs = element.attribs
            if isinstance(element, svgwrite.shapes.Rect):  # Rectángulo
                x, y = attribs.get('insert', (0, 0))
                width, height = attribs.get('size', (0, 0))
                max_x = max(max_x, x + width)
                max_y = max(max_y, y + height)
            elif isinstance(element, svgwrite.text.Text):  # Texto
                x, y = attribs.get('insert', (0, 0))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            elif isinstance(element, svgwrite.shapes.Line):  # Línea
                x1, y1 = attribs.get('start', (0, 0))
                x2, y2 = attribs.get('end', (0, 0))
                max_x = max(max_x, x1, x2)
                max_y = max(max_y, y1, y2)
            elif isinstance(element, svgwrite.shapes.Polyline):  # Polilínea
                points = list(element.points)  # Obtener los puntos como una lista
                max_x = max(max_x, *[p[0] for p in points])
                max_y = max(max_y, *[p[1] for p in points])

    return max_x, max_y


if __name__ == '__main__':
    # crearMatch(["Carlos", "María", "Luis", "Ana", "Jorge", "Elena", "Sofía", "Pedro"])
    crearMatch( ["Carlos", "María", "Luis", "Ana", "Jorge", "Elena", "Sofía", "Pedro", "Lucía", "Fernando", "Gabriela", "Raúl", "Patricia"])
