# Zadanie 4. Rejestr uczestników wydarzenia

warsztat_python = set()
warsztat_ai = set()

while True:
    print("\n==== Menu ====")
    print("1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyświetl uczestników")
    print("4. Uczestnicy obu warsztatów")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakończ")
    print("===================")

    wybor = input("Wybierz opcję: ").strip()

    if wybor == "1":
        imie = input("Imię: ").strip()
        nazwisko = input("Nazwisko: ").strip()
        uczestnik = (imie, nazwisko)
        
        if uczestnik in warsztat_python:
            print("Ta osoba jest już zapisana na warsztat Python!")
        else:
            warsztat_python.add(uczestnik)
            print("Dodano uczestnika.")

    elif wybor == "2":
        imie = input("Imię: ").strip()
        nazwisko = input("Nazwisko: ").strip()
        uczestnik = (imie, nazwisko)
        
        if uczestnik in warsztat_ai:
            print("Ta osoba jest już zapisana na warsztat AI!")
        else:
            warsztat_ai.add(uczestnik)
            print("Dodano uczestnika.")

    elif wybor == "3":
        print("\n--- Warsztat Python ---")
        if warsztat_python:
            for imie, nazwisko in sorted(warsztat_python):
                print(f"{imie} {nazwisko}")
        else:
            print("Brak zapisanych osób.")

        print("\n--- Warsztat AI ---")
        if warsztat_ai:
            for imie, nazwisko in sorted(warsztat_ai):
                print(f"{imie} {nazwisko}")
        else:
            print("Brak zapisanych osób.")

    elif wybor == "4":
        wspolni = warsztat_python & warsztat_ai
        print("\nUczestnicy obu warsztatów:")
        if wspolni:
            for imie, nazwisko in sorted(wspolni):
                print(f"{imie} {nazwisko}")
        else:
            print("Brak osób zapisanych na oba warsztaty.")

    elif wybor == "5":
        wszyscy = warsztat_python | warsztat_ai
        print("\nWszyscy unikalni uczestnicy:")
        if wszyscy:
            for imie, nazwisko in sorted(wszyscy):
                print(f"{imie} {nazwisko}")
        else:
            print("Brak jakichkolwiek zapisanych osób.")

    elif wybor == "0":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")