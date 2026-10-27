#2 Kalkulator wielofunkcyjny

petla = 1
while petla > 0:
    print("====== Kalkulator ======")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("===========================")

    opcja = int(input("Wybierz opcje: "))
    
    if opcja <= 5 and opcja >= 1:
        pierwsza = int(input("Prosze podać pierwszą liczbę: "))
        druga = int(input("Prosze podać drugą liczbę: "))
        if opcja == 1:
            print("Wynik: "+str(pierwsza)+" + "+str(druga)+" = "+str(pierwsza+druga))
        if opcja == 2:
            print("Wynik: "+str(pierwsza)+" - "+str(druga)+" = "+str(pierwsza-druga))    
        if opcja == 3:
            print("Wynik: "+str(pierwsza)+" * "+str(druga)+" = "+str(pierwsza*druga))
        if opcja == 4:
            print("Wynik: "+str(pierwsza)+" / "+str(druga)+" = "+str(pierwsza/druga))
        if opcja == 5:
            print("Wynik: "+str(pierwsza)+" ^ "+str(druga)+" = "+str(pierwsza**druga))
    if opcja == 6:
        ile = int(input("Ile liczb? "))
        suma = 0
        for x in range(ile):
            liczba = int(input("Liczba "+str(x+1)+": "))
            suma = suma + liczba
        print("Srednia: "+str(suma/ile))
    if opcja == 0:
        print("Koniec programu.")
        petla = 0
