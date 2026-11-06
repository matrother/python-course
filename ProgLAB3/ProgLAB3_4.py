#4 Menedżer budżetu osobistego

operacje = []
petla = 1

while petla > 0:
    print("===== MOJ BUDZET ====")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Usun operacje")
    print("0. Zakoncz")
    print("===========================")

    opcja = int(input("Wybierz opcje: "))
    
    if opcja == 1:
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        if kwota <= 0:
            print("Kwota musi byc dodatnia!")
        else:
            operacje.append({"opis": opis, "kwota": kwota, "rodzaj": "przychod"})
            print("Dodano przychod.")

    if opcja == 2:
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        if kwota <= 0:
            print("Kwota musi byc dodatnia!")
        else:
            operacje.append({"opis": opis, "kwota": kwota, "rodzaj": "wydatek"})
            print("Dodano wydatek.")

    if opcja == 3:
        if len(operacje) == 0:
            print("Historia jest pusta.")
        else:
            nr = 1
            for op in operacje:
                print(str(nr) + ". [" + op["rodzaj"] + "] " + op["opis"] + ": " + str(op["kwota"]) + " zl")
                nr = nr + 1

    if opcja == 4:
        przychody = 0.0
        wydatki = 0.0
        for op in operacje:
            if op["rodzaj"] == "przychod":
                przychody = przychody + op["kwota"]
            else:
                wydatki = wydatki + op["kwota"]
        stan = przychody - wydatki
        print("Aktualny stan konta:", stan, "zl")

    if opcja == 5:
        przychody = 0.0
        wydatki = 0.0
        najwiekszy_wydatek = 0.0
        byl_wydatek = False

        for op in operacje:
            if op["rodzaj"] == "przychod":
                przychody = przychody + op["kwota"]
            else:
                wydatki = wydatki + op["kwota"]
                if not byl_wydatek or op["kwota"] > najwiekszy_wydatek:
                    najwiekszy_wydatek = op["kwota"]
                    byl_wydatek = True

        bilans = przychody - wydatki
        print("Suma przychodow:", przychody, "zl")
        print("Suma wydatkow:", wydatki, "zl")
        print("Bilans:", bilans, "zl")
        if byl_wydatek:
            print("Najwiekszy wydatek:", najwiekszy_wydatek, "zl")
        else:
            print("Brak wydatkow do wyswietlenia.")

    if opcja == 6:
        szukany = input("Wpisz szukana fraze w opisie: ")
        znaleziono = False
        nr = 1
        for op in operacje:
            if szukany.lower() in op["opis"].lower():
                print(str(nr) + ". [" + op["rodzaj"] + "] " + op["opis"] + ": " + str(op["kwota"]) + " zl")
                znaleziono = True
            nr = nr + 1
        if not znaleziono:
            print("Nie znaleziono pasujacych operacji.")

    if opcja == 0:
        print("Koniec programu.")
        petla = 0