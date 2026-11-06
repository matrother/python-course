#Wypożyczalnia rowerów
wiek = int(input("Podaj swój wiek: "))
przerwanie = 0
dokument = "0"
zgoda = "0"
if wiek < 13:
    print("Masz za mało lat")
    przerwanie = 1
else:
    if wiek < 17:
        zgoda = str(input("Posiadasz zgodę opiekuna? (tak/nie): "))
        dokument = str(input("Posiadasz dokument tożsamości? (tak/nie): "))
    elif wiek >= 17:
        dokument = str(input("Posiadasz dokument tożsamości? (tak/nie): "))
if przerwanie == 1 or dokument.lower() == "nie" or zgoda.lower() == "nie" :
    print("Wypożyczenie nie możliwe")
else:
    print("Wypożyczenie możliwe")


