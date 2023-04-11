def check_anni(anni):
    try:
        if int(anni) < 0 :
            raise Exception
        return int(anni)
    except:
        print("Hai inserito un valore non ammesso. Riprova \n")
        return -1


def read_check_anni():
    while True:
        anni = check_anni(input("Inserisci l'eta del cane -> "))
        if anni != -1:
            break
    return anni


def converti(anni_umani):
    if anni_umani <= 2:
        return anni_umani * 10.5
    else:
        return (anni_umani-2) * 4 + (2 * 10.5)


def test():
    print(converti(read_check_anni()))

if __name__ == "__main__":
    test()
