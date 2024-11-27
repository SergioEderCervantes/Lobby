import random
import math
from collections import deque
import svgwrite
import os
# from settings import STATICFILES_DIRS


class Match:
    def __init__(self, id, player1,player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2
class Round:
    def __init__(self):
        self.id = 0
        self.matches = []  # Lista de los matches de la ronda

def createRounds(players = [], tournament_id = 0, parent_dir = ""):
    n = len(players)
    print(f"jugadores inscirtos: {n}")
    rounds = []
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return
    if(n % 2 == 0):
        totalRounds = n - 1
    else:
        totalRounds = n

    totalMatches = n // 2  # Matches por ronda

    # Para evitar problemas con num impar de jugadores
    if n % 2 != 0:
        players.append(None) 
        totalMatches += 1

    match_id = 0
    # Generar las rondas
    for i in range(totalRounds):
        round = Round()
        round.id = i + 1
        print(f"Ronda {i + 1}:")
        # Crear los matches para esta ronda
        for j in range(totalMatches):
            playerA = players[j]
            playerB = players[-(j + 1)]

            # Si no hay "bye", agregar el match
            if playerA is not None and playerB is not None:
                match_id += 1
                match = Match(match_id,playerA, playerB)
                round.matches.append(match)
                print(f"{match.player1} vs {match.player2}")

        # Rotar los jugadores para la siguiente ronda (excepto el primer jugador)
        players = [players[0]] + players[-1:] + players[1:-1]

        # Añadir la ronda al conjunto de rondas
        rounds.append(round)

    file_path = create_svg(rounds,tournament_id,parent_dir)
    return file_path

def create_svg(rounds, tournament_id, parent_dir):
    dwg = svgwrite.Drawing()

    XOFFSET = 250
    YOFFSET= 100

    machups_group = dwg.g(id="g__enfrentamientos")


    x_pos = x_start = 20
    y_pos = y_start = 20

    for round in rounds:
        count = 0
        y_pos = y_start + YOFFSET/2
        x_pos = x_start + XOFFSET
        rounds_group = dwg.g(id = "round__" + str(round.id))
        rounds_group.add(dwg.text(f"Ronda {round.id}",
                         insert=(x_pos, y_start),
                         fill="black",
                         font_size="16px",
                         font_weight="bold"))
        for match in round.matches:
            match_square = create_match_square(dwg, match, x_pos, y_pos)
            rounds_group.add(match_square)
            x_pos += XOFFSET
            count += 1
            if count == 3: 
                count = 0
                x_pos = x_start + XOFFSET
                y_pos += YOFFSET
                y_start += YOFFSET
        y_start += YOFFSET
        machups_group.add(rounds_group)

    dwg.add(machups_group)

    SVG_NAME = os.path.join(parent_dir,'svg', str(tournament_id) + '.svg')

    # Calcular las dimensiones que debe de tener el svg
    #width, height = get_max_dimensions(dwg.elements)
    width = 800
    height = y_pos
    

    # Guardar el archivo SVG
    id="svg_enfrentamientos"
    #dwg['width'] = width + 200
    #dwg['height'] = height + 200
    #dwg['width'] = '100%'
    #dwg['height'] = 'auto'
    calculated_height = y_pos + 50  # Agrega un margen extra si es necesario
    print(f"height: {calculated_height}")
    
    dwg['height'] = f"{calculated_height}px"
    dwg['width'] = '100%'  # Ancho relativo al contenedor
    dwg['viewBox'] = f"0 0 {width + 200} {calculated_height}"
    dwg['id'] = id
    #dwg['viewBox'] = f"0 0 {width} {height + 50}"
    dwg.saveas(filename=SVG_NAME,pretty=True)

    return SVG_NAME

def create_match_square(dwg, match_data, cx, cy):
    MATCH_WIDTH = '200px'
    MATCH_HEIGHT = "50px"
    x = cx - 0.5 * 200
    y = cy - 0.5 * 50
    match_group = dwg.g(id="match__"+ str(match_data.id), class_="matchup")
    
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