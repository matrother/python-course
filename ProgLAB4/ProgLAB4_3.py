#3  Filtrowanie wyników pomiarów

lista = []
prog_alarm = 50
ilosc = int(input("Podaj ilosc pomiarów: "))
while ilosc < 1:
    print("Podaj wlasciwa ilosc!")
    ilosc = int(input("Podaj ilosc pomiarów: "))

for x in range(ilosc):
    pomiar = int(input("Dodaj pomiar "+str(x+1)+": "))
    lista.append(pomiar)

podwojone = [x * 2 for x in lista]
wieksze = [x for x in lista if x > prog_alarm]

print("\nPomiary alarmowe: ",wieksze)
print("Pomiary pomnozone przez 2: ",podwojone)

if any(x > prog_alarm for x in lista):
    print("Czy wystapil alarm? Tak")
else:
    print("Czy wystapil alarm? Nie")

if all(x < prog_alarm for x in lista):
    print("Czy wszystkie pomiary sa prawidlowe? Tak")
else:
    print("Czy wszystkie pomiary sa prawidlowe? Nie")
