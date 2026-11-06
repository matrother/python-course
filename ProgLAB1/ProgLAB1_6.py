#Inteligentny termostat

temperatura = int(input("Podaj aktualną temperaturę: "))
domownicy = input("Jest ktoś w domu? (tak/nie) ").lower()
okno = input("Jest otwarte okno? (tak/nie) ").lower()
ogrzewanie = 0
powod = "Ogrzewanie wyłączone"

if okno == "tak":
    ogrzewanie = 0
    powod = "Otwarte okno"
elif okno == "nie" and domownicy =="tak":
    ogrzewanie = 1
    powod = "Temperatura poniżej 20 C"
elif okno == "nie" and domownicy == "nie":
    ogrzewanie = 1
    powod = "Tempertura poniżej 16 C"
else:
    ogrzewanie = 0


if ogrzewanie == 1:
    print("Ogrzewnie: WLACZONE")
    print("Powód: "+str(powod))
elif ogrzewanie == 0:
    print("Ogrzewanie: WYLACZONE")
    print("Powód: "+str(powod))
    