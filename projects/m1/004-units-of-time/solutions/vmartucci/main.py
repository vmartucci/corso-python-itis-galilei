MINUTO_IN_SEC = 60
ORA_IN_SEC = MINUTO_IN_SEC * 60
GIORNO_IN_SEC = 24 * ORA_IN_SEC


def getDurataInSecondi(num_giorni: int, num_ore: int, num_minuti: int, num_secondi: int):
    return num_giorni * GIORNO_IN_SEC + num_ore * ORA_IN_SEC + num_minuti * MINUTO_IN_SEC + num_secondi


num_giorni = int(input("Inserire numero di giorni -> "))
num_ore = int(input("Inserire numero di ore -> "))
num_minuti = int(input("Inserire numero di minuti -> "))
num_secondi = int(input("Inserire numero di secondi -> "))

print(f"Durata in secondi ->{getDurataInSecondi(num_giorni, num_ore, num_minuti, num_secondi)}")
