#Kalkulator rabatów
cena = int(input("Podaj cene produktu: "))
procent = int(input("Podaj wartość rabatu (%): "))
rabat = (cena*procent)/100
final = ((cena * 100)-(cena*procent))/100

print("Cena poczatkowa: "+str(cena)+" zł")
print("Kwota rabatu: "+str(rabat)+" zł")
print("Cena po rabacie: "+str(final)+" zł")
if rabat >= 20:
    print("Duża promocja!")
else:
    print("Standardowa promocja")