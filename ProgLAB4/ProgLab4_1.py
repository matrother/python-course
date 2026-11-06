#1 Operacje na listach i iteracja

ilosc = int(input("Podaj liczbe pomiarów: "))
lista = []

for x in range(ilosc):
    x = int(input("Podaj pomiar "+str(x+1)+": "))
    lista.append(x)

print("\n== Pierwszy i ostatni pomiar na liście ==")
print("Pierwszy: "+str(lista[0]))
print("Ostatni: "+str(lista[len(lista)-1]))

if len(lista) <= 3:
        print("\n== Wszystkie dostepne pomiary ==")
        for x in lista:
            print(x)
else:
    print("\n== Trzy pierwsze i trzy ostatnie pomiary ==")
    print("Pierwsze trzy: "+str(lista[:3]))
    print("Ostatnie trzy: "+str(lista[-3:]))

print("\n== Co drugi pomiar ==")
print("Co drugi: "+str(lista[::2]))

print("\n== Pomiary w odwrotnej kolejności ==")
print("Odwrotna kolejność: "+str(lista[::-1]))

kopia = lista.copy()
kopia[0] = 0
print("\nOryginał: "+str(lista))
print("Kopia po zmianie: "+str(kopia))