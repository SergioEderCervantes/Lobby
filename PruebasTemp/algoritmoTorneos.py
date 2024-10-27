import random
import math
from collections import deque


class Match:
    def __init__(self,id,player1,player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2


def print_ideal(matches, label):
    print(label)
    for match in matches:
        print(f"[{match.id}]: {match.player1} vs {match.player2}")

def print_no_ideal(matches, n, res, label):
    if res != 0 :
        print("Enfrentamientos adicionales:")   
    for i in range(0, res, 1):
        print(f"[{matches[i].id}]: {matches[i].player1} vs {matches[i].player2}")
    print(label) 
    for i in range(res, n,1):
        print(f"[{matches[i].id}]: {matches[i].player1} vs {matches[i].player2}")


# Creacion de emparejamiento cuando el numero de jugadores es potencia de dos
def emparejamiento_ideal(matches, jugadores, n, abecedario, stages):
    for i in range(0,n,2):
        matches.append(
            Match(next(abecedario),jugadores[i], jugadores[i+1])
        )
    print_ideal(matches,stages[int(math.log2(len(matches)))])

    
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
    bracket_principal = deque([Match('-', '-', '-') for _ in range(2**(j-1))]) 
    
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

    print_no_ideal(matches,len(matches),res,stages[j-1])


def crearMatch(jugadores = []):
    n = len(jugadores)
    stages = ['Final', 'Semifinal', 'Cuartos', 'Octavos', '16th']
    matches = []
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return

    abecedario = iter([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    random.shuffle(jugadores)
    if (n & (n - 1)) == 0 :     #los jugadores inscritos son potencia perfecta de 2, matching tradicional
        emparejamiento_ideal(matches, jugadores, n, abecedario, stages)
    else:
       emparejamiento_no_ideal(matches,jugadores,n,abecedario, stages)


if __name__ == '__main__':
    crearMatch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
    # crearMatch([1,2,3,4,5,6,7,8])