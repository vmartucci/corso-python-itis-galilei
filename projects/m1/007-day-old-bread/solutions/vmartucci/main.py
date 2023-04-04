COSTO = 3.49
PERC_SCONTO = 60 / 100

def calcola_costo(num_pane_raffermo: int):
    return num_pane_raffermo * COSTO

def calcola_sconto(prezzo: float):
    return PERC_SCONTO * prezzo

def applica_sconto(prezzo: float, sconto: float):
    return prezzo - sconto

def formatta_output(prezzo: float, sconto: float, prezzo_scontato: float):
    return "{:<20} {:=10.2f} €\n".format("prezzo", prezzo) + "{:<20} {:=10.2f} €\n".format("sconto",sconto) + "{:<20} {:=10.2f} €\n".format("prezzo scontato", prezzo_scontato)

def test():
    num_pane_raffermo = int(input("Inserisci numero pagnotte -> "))
    p = calcola_costo(num_pane_raffermo)
    s = calcola_sconto(p)
    p_s = applica_sconto(p, s)
    print(formatta_output(p,s,p_s))

if __name__ == "__main__":
    test()


