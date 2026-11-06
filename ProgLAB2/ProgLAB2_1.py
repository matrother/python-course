#1 Lista zakupów 
zakupy = []
ilosc = int(input("Podaj ilość produktów: "))
for x in range(ilosc):
    produkt = str(input("Produkt "+str(x+1)+": "))
    zakupy.append(produkt)
print("Lista: "+str(zakupy))
print("Liczba produktów: "+str(ilosc))
usun = str(input("Produkt do usuniecia: "))
if usun in zakupy:
    zakupy.remove(usun)
    print(zakupy)
elif usun not in zakupy:
    print("Nie ma takiego produktu!")