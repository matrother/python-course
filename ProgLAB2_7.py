#7 Magazyn produktów - słownik stanów
magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}
print("1. Stan magazynu")
print("2. Przyjecie towaru")
print("3. Wydanie towaru")
print("0. Zakoncz")
status = 1
while status >= 0:
    status = int(input("Wybierz opcje: "))
    if status == 1:
        if len(magazyn) == 0:
            print("Magazyn pusty!")
        else:
            for name, key in magazyn.items():
                print(str(name)+": "+str(key)+" szt.")
    if status == 2:
        in_name = str(input("Wprowadź nazwę produktu: "))
        in_count = int(input("Wprowadź ilość produktu: "))
        if in_name in magazyn:
            magazyn[in_name] += in_count
            print("Zaaktualizowano stan produktu.")
        else:
            magazyn.setdefault(in_name,in_count)
            print("Dodano do magazynu.")
    if status == 3:
        out_name = str(input("Wprowadź nazwę produktu: "))
        out_count = int(input("Wprowadź ilość do wydania: "))
        if out_name in magazyn and out_count <= magazyn[out_name]:
            magazyn[out_name] -= out_count
            print("Wydano: "+str(out_count)+" szt.")
        elif out_name not in magazyn:
            print("Nie ma takiego produktu w magazynie!")
        else:
            print("Nie ma tylu sztuk w magazynie!")
    if status == 0:
        print("Do widzenia!")
        break
    

        
    