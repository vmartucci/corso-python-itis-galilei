DIM_TO_READ = {"larghezza", "lunghezza"} #LISTA DIMENSIONI DA LEGGERE

"""
Descrizione: funzione che controlla che una dato valore sia numerico
@input val
@output val convertito in float, -1 nel caso di errore
"""
def checkDim(val):
    try:
        return float(val);
    except:
        print("Hai inserito un valore non ammesso. Riprova \n")
        return -1

"""
Descrizione: funzione che chiede all'utente di inserire una dimensione della stanza e la restituisce
@input: dimensione da leggere
@output: dimensione letta
"""
def inputDimensione(dimDaLeggere: str):
    while True:
        dim = checkDim(input(f"Inserisci {dimDaLeggere} "));
        if dim != -1:
            break
    return dim

"""
Descrizione: legge da input le dimensioni richieste e le restituisce
@input: none
@output: lista dimensioni lette
"""

def inputDimensioni():
    dimensioni = [];
    for d in DIM_TO_READ:
        dimensioni.append(inputDimensione(d));
    return dimensioni;

"""
Descrizione: funzione che calcola la superficie di una stanza
@input: larghezza e lunghezza della stanza
@output: superficie
"""
def calcolaAreaStanza(larg: float, lung: float):
    return round(larg*lung,2);

dimensioni = inputDimensioni();
superficie = calcolaAreaStanza(dimensioni[0], dimensioni[1]);
print(f"Superficie della stanza = {superficie} mq")
