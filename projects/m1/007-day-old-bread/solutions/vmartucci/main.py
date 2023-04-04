deposit_le_1Lt = 0.10
deposit_g_1Lt = 0.25

"""
Descrizione: funzione che controlla che il valore ricevuto in input sia numerico
@input n
@output n convertito in float, -1 nel caso di errore
"""
def checkInput(n):
    try:
        return float(n);
    except:
        print("Hai inserito un valore non ammesso. Riprova \n")
        return -1

"""
Descrizione: funzione che chiede all'utente di inserire un valore e lo restituisce convertito in float
@input: testo da visualizzare in output
@output: dimensione letta
"""
def readInput(testo: str):
    while True:
        n = checkInput(input(testo));
        if n != -1:
            break
    return n

"""
Descrizione: funzione che calcola il rimborso
@input: tot_le_1Lt, tot_g_1Lt num di bottiglie con capacità fino ad 1 litro e maggiore di 1 litro
@output: rimborso
"""
def getRefund(tot_le_1Lt, tot_g_1Lt):
    #calcolo il rimborso e arrotondo a due cifre dopo la virgola
    return "{:.2f}".format(tot_le_1Lt * deposit_le_1Lt + tot_g_1Lt * deposit_g_1Lt)


tot_le_1Lt = readInput("Inserisci il numero di contenitori con capacità fino ad 1 litro -> ");
tot_g_1Lt = readInput("Inserisci il numero di contenitori con capacità superiore ad 1 litro -> ");

print(f"Rimborso = {getRefund(tot_le_1Lt, tot_g_1Lt)}$")
