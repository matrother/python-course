#3 System obsługi biblioteki
ksiazki = []
petla = 1

while petla > 0:
    print("=== BIBLIOTEKA ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyswietl wszystkie ksiazki")
    print("3. Wypozycz ksiazke")
    print("4. Zwroc ksiazke")
    print("5. Usun ksiazke")
    print("0. Zakoncz")
    print("==========================")

    opcja = int(input("Wybierz opcje: "))

    if opcja == 1:
        tytul = input("Tytul: ")
        autor = input("Autor: ")
        ksiazka = {
            "tytul": tytul,
            "autor": autor,
            "dostepna": True
        }
        ksiazki.append(ksiazka)
        print("Ksiazka dodana.")
    if opcja == 2:
        if len(ksiazki) == 0:
            print("Katalog jest pusty.")
        else:
            nr = 1
            for x in ksiazki:
                if x["dostepna"]:
                    status = "Dostepna"
                else:
                    status = "Wypozyczona"
                print(str(nr) +". "+ x["tytul"] +" - "+ x["autor"]+" [" + status + "]")
                nr = nr + 1

    if opcja == 3:
        if len(ksiazki) == 0:
            print("Katalog jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            indeks = numer - 1
            if 0 <= indeks < len(ksiazki):
                if ksiazki[indeks]["dostepna"]:
                    ksiazki[indeks]["dostepna"] = False
                    print("Wypozyczono:", ksiazki[indeks]["tytul"])
                else:
                    print("Ta ksiażka jest juz wypożyczona!")
            else:
                print("Nieprawidlowy numer ksiażki!")

    if opcja == 4:
        if len(ksiazki) == 0:
            print("Katalog jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            indeks = numer - 1
            if 0 <= indeks < len(ksiazki):
                if not ksiazki[indeks]["dostepna"]:
                    ksiazki[indeks]["dostepna"] = True
                    print("Zwrocono:", ksiazki[indeks]["tytul"])
                else:
                    print("Ta ksiazka nie byla wypozyczona!")
            else:
                print("Nieprawidlowy numer ksiazki!")

    if opcja == 5:
        if len(ksiazki) == 0:
            print("Katalog jest pusty.")
        else:
            numer = int(input("Numer ksiazki: "))
            indeks = numer - 1
            if 0 <= indeks < len(ksiazki):
                usunieta = ksiazki.pop(indeks)
                print("Usunieto:", usunieta["tytul"])
            else:
                print("Nieprawidlowy numer ksiazki!")

    if opcja == 0:
        print("Koniec programu.")
        petla = 0