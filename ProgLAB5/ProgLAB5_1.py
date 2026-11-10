#1 Analiza pomiarów temperatury
import numpy as np
lista = []

ilosc = int(input("Podaj liczbę pomiarów: "))
for x in range(ilosc):
    pomiar = int(input("Pomiar " + str(x+1) + ": "))
    lista.append(pomiar)
    pomiary = np.array(lista)

print("Pomiary: "+ str(pomiary))
print("Minimum: "+str(np.min(pomiary))+" C")
print("Maksimum: "+str(np.max(pomiary))+" C")
print("Srednia: "+str(np.mean(pomiary))+" C")
print("Rozstep: "+str(np.max(pomiary)-np.min(pomiary))+" C")




