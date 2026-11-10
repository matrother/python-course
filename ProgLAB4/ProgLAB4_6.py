#6 Analiza ocen studentów–pierwszy wykresw Matplotlib
import matplotlib.pyplot as plt

liczba_studentow = int(input("Podaj liczbe studentow: "))
nazwiska = []
punkty = []
oceny = []

for i in range(1, liczba_studentow + 1):
    nazwisko = input(f"Nazwisko studenta {i}: ")
    pkt = int(input("Punkty: "))
    if pkt < 50:
        ocena = 2.0
    elif pkt < 60:
        ocena = 3.0
    elif pkt < 70:
        ocena = 3.5
    elif pkt < 80:
        ocena = 4.0
    elif pkt < 90:
        ocena = 4.5
    else:
        ocena = 5.0


    nazwiska.append(nazwisko)
    punkty.append(pkt)
    oceny.append(ocena)

srednia_ocen = sum(oceny) / len(oceny)
zaliczyli = sum(1 for o in oceny if o >= 3.0)

for nazwisko, ocena in zip(nazwiska, oceny):
    print(f"{nazwisko}- {ocena}")

print(f"Srednia ocen: {srednia_ocen:.3f}")
print(f"Liczba zaliczen: {zaliczyli}")

studenci = nazwiska
oceny = oceny
plt.bar(studenci, oceny)
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.grid(axis="y", alpha=0.3)
plt.savefig("oceny.png")
plt.show()
