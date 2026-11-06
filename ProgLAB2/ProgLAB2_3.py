#3 Automat z napojami
napoje = ["Woda","Sok","Cola"]
ceny = [3,5,6]
x=0
skarbonka = 0
while x < len(ceny):
    print(str(x+1)+". "+str(napoje[x])+" - "+str(ceny[x])+" zl")
    x = x + 1
print("0. Zakoncz")
produkt = int(input("Wybierz opcje: "))
while produkt is not 0:
    if produkt-1 < len(ceny):
        print("Wybrno: "+str(napoje[produkt-1])+", cena: "+str(ceny[produkt-1])+" zl")
        skarbonka = skarbonka + ceny[produkt-1]
    else:
        print("Wybierz prawidlowa opcje!")
    produkt = int(input("Wybierz opcje: "))
print("Lacznie do zaplaty: "+ str(skarbonka)+" zl")
        