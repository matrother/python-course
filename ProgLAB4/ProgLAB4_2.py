#2 Zestawienie produktów cen

ilosc = int(input("Podaj liczbe produktów: "))
produkty = []
ceny = []

for x in range(ilosc):
    nazwa = input("Podaj nazwe produktu "+str(x+1)+" : ")
    cena = int(input("Podaj cene produktu "+str(x+1)+" : "))
    produkty.append(nazwa)
    ceny.append(cena)

print(enumerate(produkty))