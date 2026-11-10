#4 Wyniki egzaminu - Pandas i Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

studenci = int(input("Podaj liczbę studentów: "))
while studenci < 1:
    print("\nNieprawidlowa ilosc studentów!")
    studenci = int(input("Podaj liczbe studentów: "))

tabela_punkty = []
tabela_nazwisko = []

for x in range(1,studenci+1):
    nazwisko = input("Podaj nazwisko studenta: ")
    punkty = int(input("Prosze podać liczbe punktów (0-100): "))
    while punkty < 0 or punkty > 100:
        print("\nNieprawidlowa ilosc punktow!")
        punkty = int(input("Prosze podać liczbe punktów (0-100): "))

    tabela_punkty.append(punkty)
    tabela_nazwisko.append(nazwisko)

df = pd.DataFrame({
"Nazwisko": tabela_nazwisko,
"Punkty": tabela_punkty,
})

def przypisz_ocene(punkty):
    if punkty >= 90:
        return 5.0
    elif punkty >= 80:
        return 4.5
    elif punkty >= 70:
        return 4.0
    elif punkty >= 60:
        return 3.5
    elif punkty >= 50:
        return 3.0
    else:
        return 2.0

df["Ocena"] = df["Punkty"].apply(przypisz_ocene)
print(df)

zaliczyli = (df["Ocena"] >= 3.0).sum()
print("Średnia ocen: "+ str(df["Ocena"].mean()))
print("Liczba zaliczeń: " + str(zaliczyli))

posortowane = df.sort_values("Punkty", ascending=False)
print("<========Posortowane wartości========>")
print(posortowane)

plt.bar(df["Nazwisko"], df["Ocena"])
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.tight_layout()
plt.show()