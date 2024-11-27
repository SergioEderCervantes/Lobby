class Player:
    id = 0

    def __init__(self):
        Player.id += 1
        self.player = Player.id

class Match:
    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB

class Round:
    def __init__(self):
        self.matches = []  # Lista de los matches de la ronda

# Número total de jugadores
TOTPLAYERS = 5

# Crear la lista de jugadores
players = [Player() for i in range(TOTPLAYERS)]

# Crear rondas de Round Robin
rounds = []
if(TOTPLAYERS % 2 == 0):
    totalRounds = TOTPLAYERS - 1
else:
    totalRounds = TOTPLAYERS
totalMatches = TOTPLAYERS // 2  # Matches por ronda

# Para evitar problemas con num impar de jugadores
if TOTPLAYERS % 2 != 0:
    players.append(None) 
    totalMatches += 1

# Generar las rondas
for i in range(totalRounds):
    round = Round()
    print(f"Ronda {i + 1}:")
    # Crear los matches para esta ronda
    for j in range(totalMatches):
        playerA = players[j]
        playerB = players[-(j + 1)]

        # Si no hay "bye", agregar el match
        if playerA is not None and playerB is not None:
            match = Match(playerA, playerB)
            round.matches.append(match)
            print(f"  Jugador {match.playerA.player} vs Jugador {match.playerB.player}")

    # Rotar los jugadores para la siguiente ronda (excepto el primer jugador)
    players = [players[0]] + players[-1:] + players[1:-1]

    # Añadir la ronda al conjunto de rondas
    rounds.append(round)

# Mostrar las rondas y los matches
#for round_number, round_obj in enumerate(rounds, start=1):
##    print(f"Ronda {round_number}:")
#    for match in round_obj.matches:
#        print(f"  Jugador {match.playerA.player} vs Jugador {match.playerB.player}")