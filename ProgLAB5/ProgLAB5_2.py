#2 Analiza cen produktów
import numpy as np

lista = []

ilosc = int(input("Podaj ilosc produktow: "))
while ilosc < 1:
    print("Nieprawidlowa ilość produktów!")
    ilosc = int(input("Podaj ilosc produktow: "))

for x in range(ilosc):
    cena = int(input("Cena "+str(x+1)+": "))
    lista.append(cena)
    ceny = np.array(lista)

rabat = int(input("Podaj rabat (%): "))
po_rabacie = ceny*((100-rabat)/100)
print("\nCeny poczatkowe: "+str(ceny))
print("Ceny po rabacie: "+str(po_rabacie))
print("\nSuma poczatkowa: "+str(np.sum(ceny)))
print("Suma po rabacie: "+str(np.sum(po_rabacie)))
print("Ceny powyżej 100 zl: "+str(po_rabacie[po_rabacie>100]))
