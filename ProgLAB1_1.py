#Zadanie 1
ilosc = int(input("Wpisz ilość kupionych przedmiotów: "))
cena = int(input("Wpisz cene produktu: "))
wartosc = ilosc*cena
if wartosc >= 100:
    koszt_dostawy = 0
else:
    koszt_dostawy = 12
koszt = wartosc+koszt_dostawy

print('Wartość produktów: '+ str(wartosc)+ ' zł')
print('Koszt dostaway: '+ str(koszt_dostawy)+ ' zł')
print('Do zapłaty: '+ str(koszt)+ ' zł')