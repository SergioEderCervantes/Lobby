import random
import math
from collections import deque
import svgwrite
import os


from settings import STATICFILES_DIRS
class Match:
    def __init__(self,id,player1,player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2


# Creacion de emparejamiento cuando el numero de jugadores es potencia de dos
def emparejamiento_ideal(matches, jugadores, n, abecedario, stages):
    for i in range(0,n,2):
        matches.append(
            Match(next(abecedario),jugadores[i], jugadores[i+1])
        )


    
# Creacion de emparejamiento cuando el numero de jugadores NO es potencia de dos
def emparejamiento_no_ideal(matches,jugadores, n, abecedario, stages):
    j = int(math.log2(n))
    res = n - 2**j
    adicionales = []
    jugadores_ptr = 0
    # Adicionales
    for jugadores_ptr in range(0, res*2, 2): 
        aux = Match(next(abecedario),jugadores[jugadores_ptr],jugadores[jugadores_ptr+1])
        matches.append(aux)
        adicionales.append(aux)
    jugadores_ptr = jugadores_ptr + 2
    #se los matches del bracket principal, inicialmente vacios 
    bracket_principal = deque([Match('-', '-', '-') for _ in range(2**(j-1))]) # Cambiar el 5 por la cant de matches del bracket

    for match in adicionales:
        if bracket_principal[0].id == '-': #Primera vez que pasa este elemento por el ciclo
            bracket_principal[0].id = next(abecedario)
            bracket_principal[0].player1 = match.id
        else:   # Ya se habia pasado este elemento por  el ciclo, ya tiene el player1
            bracket_principal[0].player2 = match.id
        bracket_principal.rotate(-1)

    # Terminar de llenar el bracket principal y copiarlos en la lista Matches
    for final_match in bracket_principal:
        if final_match.id == '-':   # El ciclo anterior no lo toco
            final_match.id = next(abecedario)
            final_match.player1 = jugadores[jugadores_ptr]
            final_match.player2 = jugadores[jugadores_ptr + 1]
            jugadores_ptr = jugadores_ptr + 2
        elif final_match.player2 == '-':  # El ciclo anterior lo paso una vez, ya tiene id y player1
            final_match.player2 = jugadores[jugadores_ptr]
            jugadores_ptr = jugadores_ptr + 1
        # Para este punto, el match esta completo
        matches.append(final_match)


def crearMatch(jugadores = []):
    n = len(jugadores)
    stages = ['Final', 'Semifinal', 'Cuartos', 'Octavos', '16th']
    matches = []
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return

    abecedario = iter([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    random.shuffle(jugadores)
    is_ideal = False
    if (n & (n - 1)) == 0 :     #los jugadores inscritos son potencia perfecta de 2, matching tradicional
        emparejamiento_ideal(matches, jugadores, n, abecedario, stages)
        is_ideal=True
    else:
       emparejamiento_no_ideal(matches,jugadores,n,abecedario, stages)
       
    return matches,is_ideal

# Creacion del SVG de los torneos
# Toma como argumento un arreglo de objetos Match
# Regresa el path donde se supone que se creo el svg
def create_svg_match(matchups, tournament_id, parent_dir, is_ideal):
    print("HOLA desde create_svg_match")
    WIDTH = 1200
    HEIGHT = 800
    SVG_NAME = os.path.join(parent_dir,'svg', str(tournament_id) + '.svg')
    dwg = svgwrite.Drawing(SVG_NAME, id="svg_enfrentamientos", size=(WIDTH,HEIGHT))
    # gupos para organizar los elementos
    machups_group = dwg.g(id="g__enfrentamientos")
    lines_group = dwg.g(id="g__conectores")
    LEVELS = int(math.log2(len(matchups))) + 1  if is_ideal else int(math.log2(len(matchups)))
    XOFFSET = 250
    YOFFSET=100
    SCALE = 2

    # Arreglo de arreglos, cada posicion tendra un arreglo de match_squares, los cuales son un svg group
    connector_points = []
    cx = 250;
    for level in range (LEVELS):
        aux = []
        cy = YOFFSET * math.pow(SCALE,level)/2
        matches_in_level = int(len(matchups) / math.pow(2,level))
        for i in range(0,matches_in_level):
            match_data = matchups[i] if level == 0 else Match("","","")
            match_square = create_match_square(dwg, match_data, cx, cy)
            aux.append(match_square)
            machups_group.add(match_square)
            cy = cy + YOFFSET * math.pow(SCALE,level)
        cx = cx + XOFFSET
        connector_points.append(aux)

    for i in range(0, len(connector_points)):
        if i + 1 != len(connector_points):
            connect_levels(dwg, lines_group, True, connector_points[i], connector_points[i+1])
    
    dwg.add(machups_group)
    dwg.add(lines_group)
    dwg.save(pretty=True)
    
    return SVG_NAME

    

# Crea los componentes graficos para un rectangulo de matchup con todos los datos que se le envian de parametros
# Regresa un grupo con todos los elementos
def create_match_square(dwg, match_data, cx, cy):
    MATCH_WIDTH = '200px'
    MATCH_HEIGHT = "50px"
    x = cx - 0.5 * 200
    y = cy - 0.5 * 50
    match_group = dwg.g(id="match__"+match_data.id)
    
    # Rectangulo de fondo
    match_group.add(dwg.rect(insert=(x,y), size=(MATCH_WIDTH,MATCH_HEIGHT), fill = '#444444', rx=10, ry=10,class_="fondo_matchup"))
    # Rectangulo de id
    match_group.add(dwg.rect(insert=(x,y), size=('25px', MATCH_HEIGHT), fill='#a1a1a1', rx=10, ry=10, class_="matchup__id__container"))
    match_group.add(dwg.text(match_data.id, insert=(x+8, y+30), class_="matchup__id", font_weight = 700))
    # Rectangulo de los jugadores
    match_group.add(dwg.rect(insert=(x+25,y), size=('175px',MATCH_HEIGHT), rx=10, ry=10, fill='#444444', class_="players__container"))
    # Jugadores
    group1 = dwg.g(class_="matchup__player")
    group1.add(dwg.rect(insert=(x+25,y), size=('175px','25px'), fill='#444444',rx=10, ry=10))
    group1.add(dwg.text(match_data.player1, insert=(x+30, y+18), class_="matchup__player1", fill="white", font_size="14px"))
    match_group.add(group1)
    
    group2 = dwg.g(class_="matchup__player")
    group2.add( dwg.rect(insert=(x+25,y+25), size=("175px","25px"), fill="#444444", rx=10, ry=10))
    group2.add(dwg.text(match_data.player2, insert=(x+30, y+45), class_="matchup__player2", fill="white", font_size="14px"))
    match_group.add(group2)
    
    # Linea entre los jugadores
    match_group.add(dwg.line(start=(x+25, y+25), end=(x+175, y+25),stroke="black", stroke_width=1, class_="divisor_line"))
    
    # Linea para diferenciar la parte de jugadores de la parte de la insersion de puntaje
    match_group.add(dwg.line(start=(x+175,y), end = (x+175,y+50), stroke="black", stroke_width=1, class_="divisor_line_2"))
    # Campo para insersion del puntaje
    match_group.add(dwg.rect(insert=(x+175,y), size=("25px", "25px"), fill='#a1a1a1', rx=10,ry=10, class_="match__puntaje__player1"))
    match_group.add(dwg.rect(insert=(x+175,y+25), size=("25px", "25px"), fill='#a1a1a1', rx=10,ry=10, class_="match__puntaje__player2"))
    
    return match_group
    
# Funcion que, dado dos niveles del torneo, 
def connect_levels(dwg,group, isIdeal, level1, level2):
    pivot = 0
    if isIdeal:
        for match in level2:
            center1 = get_group_center(level1[pivot]) 
            point1 = (center1[0]+100, center1[1])
            
            
            center2 = get_group_center(level1[pivot+1]) 
            point2 = (center2[0]+100, center2[1])
            
            center3 = get_group_center(match)
            center_point= (center3[0] - 100, center3[1])
            
            group.add(dwg.polyline([point1,center_point],fill='none', stroke="white", stroke_width=2))
            group.add(dwg.polyline([point2,center_point],fill='none', stroke="white", stroke_width=2))
            pivot +=2


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