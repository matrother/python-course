#5 System logowania - trzy próby
haslo = "Python123"
licznik = 0
while licznik < 3:
    licznik = licznik + 1
    proba = str(input("Podaj hasło: "))
    if proba == haslo:
        print("Logowanie udane!")
        break
    else:
        print("Niepoprawne haslo. Pozostale proby: "+str(3-licznik))
