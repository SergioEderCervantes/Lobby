import random

def crearMatch(jugadores = []):
    n = len(jugadores)
    if n <= 1:   #No puede crear el torneo
        print("No puede crear el torneo")
        return
    
    stages = ['Final, Semifinal, Cuartos, Octavos, 16th']
    matches = []
    random.shuffle(jugadores)
    
    if (n & (n - 1)) == 0 :     #los jugadores inscritos son potencia perfecta de 2, matching tradicional
        print("Matchs:")
        for i in range(0,n,2):
            matches.append((jugadores[i],jugadores[i+1]))
    else:
        print("La cantidad de jugadores no es potencia de dos")
        j = 1
        
        while (n - 2**j) > 0:
            j = j + 1
            
        j = j - 1 #Para ajustar
        res = n - 2**j
        
        for i in range(0,res*2, 2):   
            matches.append((jugadores[i],jugadores[i+1]))
        
        for i in range(i+2, res*3, 1):
            matches.append(("-",jugadores[i]))
        
        for i in range(i + 1, n, 2):
            matches.append((jugadores[i],jugadores[i+1]))
       
        
    for match in matches:
        print(match);


crearMatch([1,2,3,4,5,6,7,8])