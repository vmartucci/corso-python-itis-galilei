#DIZIONARIO I CUI ELEMENTI CHIAVE : VALORE SONO COSì SPECIFICATI ->    VALORE_MONETA : NOME_MONETA
nomi_monete = {200: "toonie" , 100: "loonie", 25 : "quarter", 10: "dime", 5: "nickel", 1 : "pennie"}

#DIZIONARIO I CUI ELEMENTI CHIAVE : VALORE SONO COSì SPECIFICATI ->   VALORE_MONETA :  QUANTITA_MONETA
monete = {200 : 0, 100 : 0, 25 : 0, 10 : 0, 5 : 0, 1 : 0}

importo = int(input("Inserisci importo -> "));

while importo > 0 :
    for moneta in monete.keys() :
        if importo >= moneta :
            importo -= moneta
            monete[moneta] += 1
            break

print("\nMonete restituite:")
for moneta in monete.keys() :
    if monete[moneta] != 0 :
        print(f"{monete[moneta]} {nomi_monete[moneta]} ({moneta}cent) \n")