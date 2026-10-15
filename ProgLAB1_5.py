#Kalkulator opłat parkingowych
czas = int(input("Podaj liczbe godzin parowania (h): "))
if czas > 0:
     if czas <= 1:
        cena = 5
     elif czas <= 3:
        cena = 12
     elif czas <=6:
        cena = 20
     elif czas > 6:
        cena = 30
     print("Czas postoju: "+str(czas)+" godziny")
     print("Opłata za parking: "+str(cena)+" zł")
else:
 print("Podaj właściwe dane!")
