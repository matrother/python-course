#6 System zarzadzania zadaniami
zadania = []

print("1 - Dodaj zadnaie")
print("2 - Wyświetl zadanie")
print("3 - Usuń zadanie")
print("4 - Wyświetl liczbe zadań")
print("0 - Zakończ")

status = 1
while status >= 0:
    status = int(input("Wybierz opcje: "))
    if status == 1:
        nazw_zadania = str(input("Podaj nazwe zadania: "))
        zadania.append(nazw_zadania)
    elif status == 2:
        i = 0
        if len(zadania) == 0:
            print("Brak zadań")
        else:
            for x in zadania:
                i = i+1
                print(str(i)+". "+str(x))
    elif status == 3:
        usun = int(input("Podaj numer zadania do usunięcia: "))
        if len(zadania) >= usun:
            zadania.remove(zadania[usun-1])
        else:
            print("Podaj prawidłowy numer!")
    elif status == 4:
        print("Liczba zadań: "+str(len(zadania)))
    elif status > 4:
        print("Podaj właściwy numer opcji!")
    elif status == 0:
        print("Do widzenia!")
        break
