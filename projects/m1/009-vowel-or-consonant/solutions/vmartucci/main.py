def check(lettera):
    try:
        if not(lettera.isalpha()) or len(lettera) != 1: #se non è un carattere alfabetico o se ha una lung != 1
            raise Exception
        return lettera
    except:
        print("Hai inserito un valore non ammesso. Riprova \n")
        return -1

def read_check_lower():
    while True:
        lettera = check(input("Inserisci una lettera -> "))
        if lettera != -1:
            break
    return lettera.lower()

def is_vocale(lettera):
    return lettera in ["a","e","i","o","u"]

def is_y(lettera) :
    return lettera == 'y'

def get_msg(lettera) :
    return "VOCALE" if is_vocale(lettera) else "VOCALE/CONSONANTE" if is_y(lettera) else "CONSONANTE"

def test():
    lettera = read_check_lower()
    print(get_msg(lettera))

if __name__ == "__main__":
    test()
