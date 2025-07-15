import random
import statistics
from fpdf import FPDF

# Lista giocatori (1 = forte, 7 = scarso)
giocatori = [
    {"nome": "Luca", "livello": 3},
    {"nome": "Manuel", "livello": 2},
    {"nome": "Zanna C", "livello": 1},
    {"nome": "Giulia ex", "livello": 7},
    {"nome": "Lisa T", "livello": 2},
    {"nome": "Carlo C", "livello": 5},
    {"nome": "Valentina98", "livello": 7},
    {"nome": "Alberto Lentini", "livello": 7},
    {"nome": "Marta", "livello": 2},
    {"nome": "Maly", "livello": 7},
    {"nome": "Gaffeo pallanuoto", "livello": 4},
    {"nome": "Sara Mauro", "livello": 2},
    {"nome": "A. Fava", "livello": 2},
    {"nome": "Federico A.", "livello": 1},
    {"nome": "Davide B.", "livello": 4},
    {"nome": "Carlino", "livello": 5},
    {"nome": "Vittoria G.", "livello": 3},
    {"nome": "Anna Bosc", "livello": 3},
    {"nome": "tatuatore chinez", "livello": 5},
    {"nome": "France Ferra", "livello": 4},
    {"nome": "Comi jr.", "livello": 1},
]





# ----------------------------------------------------------------------------------------
# INFO :
# totale giocatori
totale_giocatori = len(giocatori)
print(f"\n🎯 Ci sono {totale_giocatori} giocatori totali.\n")

print("📊 Possibili distribuzioni se scegli tra 2 e 6 giocatori per squadra:\n")
for giocatori_per_squadra in range(2, 7):
    num_squadre = round(totale_giocatori / giocatori_per_squadra)
    base = totale_giocatori // num_squadre
    extra = totale_giocatori % num_squadre
    distribuzione = [base + 1 if i < extra else base for i in range(num_squadre)]
    if min(distribuzione) < 2:
        continue  # Evita squadre troppo piccole
    print(f"- {num_squadre} squadre da circa {giocatori_per_squadra} → {distribuzione}")


# quanti giocatori per squadra
giocatori_per_squadra = int(input("Quanti giocatori desideri per squadra (es. 4 o 5)? "))

# Calcola il numero di squadre
num_squadre = round(totale_giocatori / giocatori_per_squadra)

# Calcola distribuzione ipotetiche
base = totale_giocatori // num_squadre
extra = totale_giocatori % num_squadre
distribuzione_target = [base + 1 if i < extra else base for i in range(num_squadre)]

print("\n📊 Distribuzione prevista:", distribuzione_target)


# -------------------------------------------------------------
# Funzioni
def crea_squadre(mixed, distribuzione):
    squadre = []
    index = 0
    for size in distribuzione:
        squadre.append(mixed[index:index + size])
        index += size
    return squadre

def calcola_deviazione(squadre):
    medie = [statistics.mean([g["livello"] for g in squadra]) for squadra in squadre]
    return statistics.stdev(medie)

# -------------------------------------------------------------
# DOCTOR STRANGE
ITERAZIONI = 1000
migliore_squadre = None
deviazione_migliore = float("inf")

for _ in range(ITERAZIONI):
    random.shuffle(giocatori)
    squadre_correnti = crea_squadre(giocatori, distribuzione_target)
    deviazione = calcola_deviazione(squadre_correnti)
    if deviazione < deviazione_migliore:
        migliore_squadre = squadre_correnti
        deviazione_migliore = deviazione

# -------------------------------------------------------------
# Risultato
print(f"\n✅ Miglior combinazione trovata dopo {ITERAZIONI} tentativi")
print(f"📉 Deviazione standard delle medie: {deviazione_migliore:.3f}")
print(f"🧮 Distribuzione squadre: {distribuzione_target}")

for i, squadra in enumerate(migliore_squadre):
    media = statistics.mean([g["livello"] for g in squadra])
    print(f"\n🏅 Squadra {i+1} (Media livello: {media:.2f}):")
    for g in squadra:
        print(f"  - {g['nome']} (livello {g['livello']})")

# -------------------------------------------------------------
# Nomi personalizzati
nomi_squadre = []
print("\n📌 Dai un nome a ciascuna squadra:")
for i in range(len(migliore_squadre)):
    nome = input(f"Nome per la Squadra {i+1}: ")
    nomi_squadre.append(nome.strip() if nome.strip() else f"Squadra {i+1}")

# -------------------------------------------------------------
# PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Divisione Squadre - Miglior Bilanciamento", ln=True, align="C")
pdf.ln(10)
pdf.cell(200, 10, txt=f"Deviazione standard delle medie: {deviazione_migliore:.3f}", ln=True)
pdf.cell(200, 10, txt=f"Distribuzione squadre: {distribuzione_target}", ln=True)

for i, squadra in enumerate(migliore_squadre):
    media = statistics.mean([g["livello"] for g in squadra])
    pdf.ln(8)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=f"{nomi_squadre[i]} (Media livello: {media:.2f}):", ln=True)
    pdf.set_font("Arial", size=12)
    for g in squadra:
        pdf.cell(200, 10, txt=f"  - {g['nome']}", ln=True)

pdf.output("divisione_squadre.pdf")
print("\n📄 PDF generato: divisione_squadre.pdf")