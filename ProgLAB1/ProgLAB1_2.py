#Ocena z egzaminu
punkty = int(input("Prosze podać liczbe punktów: "))
ocena = 0.0
if punkty > 0:
    if punkty <= 49:
        ocena = 2.0
    elif punkty <= 59:
        ocena =3.0
    elif punkty <=69:
        ocena = 3.5
    elif punkty <= 79:
        ocena = 4.0
    elif punkty <= 89:
        ocena = 4.5
    elif punkty <= 100:
        ocena = 5.0
    else: 
        print("Podaj właściwą wartość punktów")
else:
    print("Podaj właściwą ilość punktów")

print("Liczba punktów: "+str(punkty))
print("Uzyskana ocena: "+str(ocena))