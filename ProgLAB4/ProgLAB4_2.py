#2 Zestawienie produktów cen

ilosc = int(input("Podaj ilosc produktów: "))
while ilosc < 1:
    print("Podaj wlasciwa ilosc!")
    ilosc = int(input("Podaj liczbe produktów: "))

produkty = []
ceny = []

for x in range(ilosc):
    nazwa = input("Podaj nazwe produktu "+str(x+1)+" : ")
    cena = int(input("Podaj cene produktu "+str(x+1)+" : "))
    produkty.append(nazwa)
    ceny.append(cena)

print("\n <=====Ponumerowana lista produktów=====>")
for numer, produkt in enumerate(produkty, start=1):
    print(numer, produkt)

i=0
print("\n <===Cennik produktów===>")
for produkt, cena in zip(produkty, ceny):
    i = i+1
    print(str(i)+".",produkt," - ", cena, "zl")

for produkt, cena in zip(produkty, ceny):
    if cena == max(ceny):
        cena_maks = cena
        produkt_maks = produkt

print("\nSuma cen: ",sum(ceny))
print("Najdrozszy produkt: ",produkt_maks,"-",cena_maks,"zl")