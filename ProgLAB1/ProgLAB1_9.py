#9 Liczby parzyste i nieparzyste
poczatek = int(input("Podaj początek zakresu: "))
koniec = int(input("Podaj koniec zakresu: "))
parzyste = 0 

for x in range(poczatek,koniec+1,1):
    modulo = x % 2
    if modulo == 0:
        print("Liczba: "+str(x))
        print("Jest parzysta")
        print("=-=-=-=-=-=-=-=")
        parzyste += 1

    else:
        print("Liczba: "+str(x))
        print("Nie jest parzysta")
        print("=-=-=-=-=-=-=-=")
print("Liczba list parzystych: "+str(parzyste))
