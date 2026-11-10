#5 Kalkulator wielofunkcyjny – wprowadzenie do funkcji

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return None
    return a / b

def potegowanie(a, b):
    return a ** b

def srednia(liczby):
    if not liczby:
        return 0.0
    return sum(liczby) / len(liczby)

def wyswietl_menu():
    print("\n==== Menu Kalkulatora ====")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Średnia arytmetyczna")
    print("0. Zakończ")
    print("==========================")

def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ").strip()

        if wybor in ["1", "2", "3", "4", "5"]:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

            if wybor == "1":
                wynik = dodawanie(a, b)
                print(f"Wynik: {wynik}")
            elif wybor == "2":
                wynik = odejmowanie(a, b)
                print(f"Wynik: {wynik}")
            elif wybor == "3":
                wynik = mnozenie(a, b)
                print(f"Wynik: {wynik}")
            elif wybor == "4":
                wynik = dzielenie(a, b)
                if wynik is None:
                    print("Błąd: Nie można dzielić przez zero!")
                else:
                    print(f"Wynik: {wynik}")
            elif wybor == "5":
                wynik = potegowanie(a, b)
                print(f"Wynik: {wynik}")

        elif wybor == "6":
            ile = int(input("Ile liczb chcesz podać? "))
            if ile <= 0:
                print("Liczba elementów musi być większa od zera.")
            else:
                lista_liczb = []
                for i in range(ile):
                    liczba = float(input(f"Liczba {i + 1}: "))
                    lista_liczb.append(liczba)
                
                wynik = srednia(lista_liczb)
                print(f"Średnia: {wynik}")

        elif wybor == "0":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()