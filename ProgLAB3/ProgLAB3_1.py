#1 Książka kontaków
kontakty = {}
petla = 1

while petla > 0:
    print("==== KSIAZKA KONTAKTOW ====")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt ")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("===================")

    opcja = int(input("Wybierz opcje ")) 

    if opcja == 1:
        imie = input("Imie:") 
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")
        if telefon in kontakty:
            print("Kontakt o tym numerze juz istnieje!")
        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.") 

    if opcja == 2:
        if len(kontakty) == 0:
            print("Ksiazka kontaktow jest pusta.")
        else:
            for tel in kontakty: 
                dane = kontakty[tel]
                print("Telefon:", tel, "-", dane[0], dane[1]) 
 
    if opcja == 3:
        telefon = input("Podaj numer telefonu do wyszukania:")
        if telefon in kontakty:
            dane = kontakty[telefon]
            print("Znaleziono:", dane[0], dane[1], "Telefon: ", telefon)
        else:
            print("Nie znaleziono kontaktu.")

    if opcja == 4:
        telefon = input("Podaj numer telefonu do edycji: ")
        if telefon in kontakty:
            nowe_imie = input("Podaj nowe imie:")
            nowe_nazwisko = input("Podaj nowe nazwisko: ")
            kontakty[telefon] = [nowe_imie, nowe_nazwisko]
            print("Kontakt zaktualizowany.") 
        else:
            print("Nie ma takiego kontaktu.")

    if opcja == 5:
        telefon = input("Podaj numer telefonu do usuniecia: ")
        if telefon in kontakty:
            del kontakty[telefon] 
            print("Kontakt usuniety.")
        else:
            print("Nie ma takiego kontaktu.") 
 
    if opcja == 0:
        print("Koniec programu.")
        petla = 0