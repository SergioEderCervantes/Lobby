import random
import math


class Match(object):
    def __init__(self,id,player1,player2):
        self.id = id
        self.player1 = player1
        self.player2 = player2

  
  
  
      
def print1(matches):
    stages = ['Final', 'Semifinal', 'Cuartos', 'Octavos', '16th']
    aux = int(math.log2(len(matches)))
    print(stages[aux])
    for match in matches:
        print(f"[{match.id}]: {match.player1} vs {match.player2}")

def print2(matches, n, res, j):
    stages = ['Final', 'Semifinal', 'Cuartos', 'Octavos', '16th']
    if res != 0 :
        print("Enfrentamientos adicionales:")   
    for i in range(0, res, 1):
        print(f"[{matches[i].id}]: {matches[i].player1} vs {matches[i].player2}")
    print(stages[j-1]) 
    for i in range(res, n - res - 1,1):
        print(f"[{matches[i].id}]: {matches[i].player1} vs {matches[i].player2}")



def crearMatch(jugadores = []):
    n = len(jugadores)
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return
    
    
    matches = []
    abecedario = iter([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    abecedario2 = iter([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    
    # random.shuffle(jugadores)
    res = 0
    j = 1
    if (n & (n - 1)) == 0 :     #los jugadores inscritos son potencia perfecta de 2, matching tradicional
        print("Matchs:")
        for i in range(0,n,2):
            matches.append(
                Match(next(abecedario),jugadores[i], jugadores[i+1])
            )
        print1(matches)
    else:
        print("La cantidad de jugadores no es potencia de dos")
        j = 1
        
        while (n - 2**j) > 0:
            j = j + 1
            
        j = j - 1 #Para ajustar
        res = n - 2**j
        
        for i in range(0,res*2, 2):   
            matches.append(
                Match(next(abecedario),jugadores[i],jugadores[i+1])
            )    
        for i in range(i+2, res*3, 1):
            matches.append(
                Match(next(abecedario),f"[{next(abecedario2)}]", jugadores[i])
            )       
        for i in range(i + 1, n - 1, 2):
            matches.append(
                Match(next(abecedario),jugadores[i],jugadores[i+1])
            )
        print2(matches, n, res, j)
       



crearMatch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])


# crearMatch([1,2,3,4,5,6,7,8])