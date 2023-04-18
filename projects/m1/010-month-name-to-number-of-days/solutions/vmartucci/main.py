"""
The length of a month varies from 28 to 31 days.
In this exercise you will create a program that reads the name of a month from the user as a string.
Then your program should display the number of days in that month.
Display “28 or 29 days” for February so that leap years are addressed.

"""

MESI = {"NOVEMBRE": "N.ro giorni 30", "APRILE": "N.ro giorni 30", "GIUGNO": "N.ro giorni 30",
        "SETTEMBRE": "N.ro giorni 30", "GENNAIO": "N.ro giorni 31", "MARZO": "N.ro giorni 31",
        "MAGGIO": "N.ro giorni 31", "FEBBRAIO": "N.ro giorni 28/29"}


def getGiorni(mese: str):
    try:
        return MESI[mese.upper()]
    except:
        print("Hai inserito un valore non ammesso. Riprova \n")
        return ""


def test():
    while True:
        num_giorni = getGiorni(input("Inserire mese -> "))
        if num_giorni != "":
            break
    print(num_giorni)


if __name__ == "__main__":
    test()
