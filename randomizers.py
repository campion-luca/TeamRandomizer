import random
import statistics
import math

# Lista giocatori (1 = forte, 7 = scarso)
giocatori = [
    {"nome": "Luca", "livello": 3},
    {"nome": "Manuel", "livello": 2},
    {"nome": "Zanna C", "livello": 1},
    {"nome": "Giulia ex", "livello": 6},
    {"nome": "Lisa T", "livello": 2},
    {"nome": "Carlo C", "livello": 5},
    {"nome": "Valentina98", "livello": 7},
    {"nome": "Alberto Lentini", "livello": 7},
    {"nome": "Marta", "livello": 1},
    {"nome": "Maly", "livello": 7},
    {"nome": "Gaffeo pallanuoto", "livello": 3},
    {"nome": "Sara Mauro", "livello": 2},
    {"nome": "A. Fava", "livello": 2},
    {"nome": "Federico A.", "livello": 1},
    {"nome": "Davide B.", "livello": 4},
    {"nome": "Carlino", "livello": 5},
    {"nome": "Vittoria G.", "livello": 3},
    {"nome": "Anna Bosc", "livello": 3},
    {"nome": "tatuatore chinez", "livello": 5},
]

# Input: giocatori per squadra
giocatori_per_squadra = int(input("Quanti giocatori per squadra? "))

# Prepara i dati
totale_giocatori = len(giocatori)
giocatori_utilizzati = (totale_giocatori // giocatori_per_squadra) * giocatori_per_squadra
num_squadre = giocatori_utilizzati // giocatori_per_squadra
giocatori_attivi = giocatori[:giocatori_utilizzati]
giocatori_esclusi = giocatori[giocatori_utilizzati:]

# Funzione: crea squadre da una lista
def crea_squadre(mixed):
    return [mixed[i:i+giocatori_per_squadra] for i in range(0, len(mixed), giocatori_per_squadra)]

# Funzione: calcola deviazione delle medie
def calcola_deviazione(squadre):
    medie = [statistics.mean([g["livello"] for g in squadra]) for squadra in squadre]
    return statistics.stdev(medie)

# Ricerca della miglior combinazione - DOCTOR STRANGE
migliore_squadre = None
deviazione_migliore = float("inf")
ITERAZIONI = 1000

for _ in range(ITERAZIONI):
    copia = giocatori_attivi[:]
    random.shuffle(copia)
    squadre = crea_squadre(copia)
    deviazione = calcola_deviazione(squadre)
    if deviazione < deviazione_migliore:
        migliore_squadre = squadre
        deviazione_migliore = deviazione

# Stampa risultato finale
print(f"\n✅ Miglior combinazione trovata dopo {ITERAZIONI} tentativi")
print(f"📉 Deviazione standard delle medie: {deviazione_migliore:.3f}")

for i, squadra in enumerate(migliore_squadre):
    media = statistics.mean([g["livello"] for g in squadra])
    print(f"\n🏅 Squadra {i+1} (Media livello: {media:.2f}):")
    for g in squadra:
        print(f"  - {g['nome']} (livello {g['livello']})")

if giocatori_esclusi:
    print(f"\n🚫 Giocatori esclusi ({len(giocatori_esclusi)}):")
    for g in giocatori_esclusi:
        print(f"  - {g['nome']} (livello {g['livello']})")
