def converti_in_int(num_stringa: str):
    num = [0,0,0,0]
    for i, c in enumerate(num_stringa):
        try:
            num[i] = int(c)
        except:
            print("Errore: Hai inserito un valore non intero \n")
            return -1
    return num


def leggi_4_cifre():
    num_stringa = str(input("Inserisci un numero a 4 cifre -> "))

    while len(num_stringa) != 4 :
        print('Errore: non hai inserito 4 cifre \n')
        num_stringa = str(input("Inserisci un numero a 4 cifre -> "))

    return num_stringa


def get_input():
    number = -1
    while number == -1:
        number = converti_in_int(leggi_4_cifre())
    return number


def sommaCifre(number):
    somma = 0
    for c in number:
        somma += c
    return somma


number = get_input()
print(f'Somma = {sommaCifre(number)}')
