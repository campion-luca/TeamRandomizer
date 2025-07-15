import random

# giocatori disponibili
giocatori = [{"nome": "Luca", "livello": 3},
             {"nome": "Manuel", "livello": 2},
             {"nome": "Zanna C", "livello": 1},
             {"nome": "Giulia ex", "livello": 5},
             {"nome": "Lisa T", "livello": 2},
             {"nome": "Carlo C", "livello": 4},
             {"nome": "Valentina98", "livello": 5},
             {"nome": "Zoppo", "livello": 5},
             {"nome": "Marta", "livello": 1},
             {"nome": "Maly", "livello": 5},
             {"nome": "Gaffeo pallanuoto", "livello": 3},
             {"nome": "Sara Mauro", "livello": 2},
             {"nome": "A. Fava", "livello": 2},
             {"nome": "Federico A.", "livello": 1},
             {"nome": "Davide B.", "livello": 3},
             {"nome": "Carlino", "livello": 4},
             {"nome": "Vittoria G.", "livello": 3},
             {"nome": "Anna Bosc", "livello": 3},
             {"nome": "tatuatore chinez", "livello": 4},
             
             ]

# Raggruppa per livello
gruppi = {1: [], 2: [], 3: [], 4: [], 5: []}
for g in giocatori:
    gruppi[g["livello"]].append(g)

# Mescola ogni gruppo
for livello in gruppi:
    random.shuffle(gruppi[livello])

# Crea 8 squadre
num_squadre = 8
squadre = [[] for _ in range(num_squadre)]

# Assegna i giocatori alle squadre in modo bilanciato
for livello in range(5, 0, -1):
    for i, giocatore in enumerate(gruppi[livello]):
        squadre[i % num_squadre].append(giocatore)

# Mostra le squadre
for i, squadra in enumerate(squadre):
    print(f"\nSquadra {i+1}:")
    for g in squadra:
        print(f"  {g['nome']} (livello {g['livello']})")