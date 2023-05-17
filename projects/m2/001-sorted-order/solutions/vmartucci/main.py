# definisco eccezione custom ZeroFirstError
class ZeroFirstError(Exception):
    pass


""" FUNZIONE user_input
Legge un valore da input e restituisce
- il valore letto, se è un numero
- solleva eccezione ZeroFirstError, se è zero ed è il primo valore letto
- solleva eccezione ValueError, se è una cifra alfabetica
"""


def user_input(is_first):
    try:
        num = int(input("Inserisci un numero -> "))
        if is_first and num == 0:  # Se è il primo numero ed è zero
            raise ZeroFirstError  # sollevo eccezione ZeroFirstError (da intercettare con except)
        return num
    except ValueError:  # Se non è un numero
        raise ValueError  # sollevo eccezione ValueError (da intercettare con except)


def test():
    list = []
    is_First = True;  # inizializzo is_Fist a True

    while True:  # Finchè l'utente non inserisce 0

        try:
            num = user_input(is_First)
            is_First = False;  # Setto is_First a False
            # alle successive chiamate di user_input() gli passo is_First a false)
            if num == 0:
                break
            list.append(num)

        except ZeroFirstError:  # Eccezione sollevata quando è il primo ed è zero
            is_First = True;  # Settandolo di nuovo a True, rileggo il primo carattere
            print("Hai inserito zero come primo carattere. Riprova.\n")

        except ValueError:  # Eccezione sollevata quando è un carattere alfabetico
            print("Hai inserito un carattere non valido. Riprova.\n")

    print("\nLista valori: ")
    print(list)
    print("\nLista valori ordinata: ")
    list.sort(reverse=True)
    print(list)


if __name__ == "__main__":
    test()