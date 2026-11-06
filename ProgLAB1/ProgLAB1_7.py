#7 Plan oszczedzania 
kwota = int(input("Jaką kwotę chcesz odkładać co tydzień? "))
okres = int(input("Podaj ile tygodni chcesz oszczędzać: "))
suma = 0
for x in range(1,okres+1):
    suma += kwota
    print("Po tygodniu: "+str(x))
    print("Odłożyłeś: "+str(suma))
    print("=-=-=-=-=-=-=-=-=")
print("Całkowita zaoszczędzona kwota to: "+str(suma))