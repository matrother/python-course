#3 Ewidencja produktów w sklepie

import pandas as pd

df = pd.DataFrame({
"Produkt": ["Mysz", "Klawiatura","Monitor","Podkladka"],
"Cena": [50, 120, 650, 30],
"Ilosc": [10, 5, 3, 20]
})
df["Wartosc"] = df["Cena"] * df["Ilosc"]
print(df)

print("\nProdukty drozsze niz 100 zl:")
print(df[df["Cena"] > 100]["Produkt"])

print("\nWartosc magazynu: "+str(df["Wartosc"].sum()))
print("Srednia cena: "+str(df["Cena"].mean()))