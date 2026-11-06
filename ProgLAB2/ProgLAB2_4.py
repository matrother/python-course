#4 Dziennik temperatur
temperatury = []
dzien = 0
powyzej_sredniej = []
for x in range(7):
    dzien = int(input("Dzien "+str(x+1)+": "))
    temperatury.append(dzien)
srednia = sum(temperatury)/len(temperatury)
print("Srednia: "+str(srednia)+" C")
print("Najniższa: "+str(min(temperatury))+" C")
print("Najwyższa: "+str(max(temperatury))+" C")

dni = 0
for x in temperatury:
    if x > srednia:
        powyzej_sredniej.append(x)
        dni = dni + 1
print("Powyzej sredniaj: "+str(powyzej_sredniej))
print("Liczba dni: "+str(dni))
