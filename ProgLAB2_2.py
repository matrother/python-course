#2 Analiza wyników egzaminu
studenci = int(input("Podaj liczbę studentów: "))
zaliczyli = 0
tabela = []

for x in range(1,studenci+1):
    nazwisko = input("Podaj nazwisko studenta: ")
    punkty = int(input("Prosze podać liczbe punktów: "))
    tabela.append(punkty)
    ocena = 0.0
    if punkty > 0:
        if punkty <= 49:
            ocena = 2.0
        elif punkty <= 59:
            ocena =3.0
            zaliczyli += 1
        elif punkty <=69:
            ocena = 3.5
            zaliczyli += 1
        elif punkty <= 79:
            ocena = 4.0
            zaliczyli += 1
        elif punkty <= 89:
            ocena = 4.5
            zaliczyli += 1
        elif punkty <= 100:
            ocena = 5.0
            zaliczyli += 1
        else: 
            print("Nieprawidłowa liczba punktów!")
    else:
        print("Nieprawidłowa liczba punktów!")

    if 0<=punkty<=100:
        print("Nazwisko studenta "+str(x)+": "+str(nazwisko))
        print("Liczba punktów: "+str(punkty))
        print(str(nazwisko)+" - " +str(punkty)+" pkt - ocena " + str(ocena))

tabela.sort()
print("Średnia: "+ str(sum(tabela) / len(tabela)))
print("Najwyższy wynik: "+ str(max(tabela)))
print("Najniższy wynik: "+ str(min(tabela)))
print("Wyniki rosnaco: "+ str(tabela))
print("Liczba zaliczeń: "+ str(zaliczyli))