def srednia(xs):
    if not xs:
        raise ValueError("brak pomiarów")
    return sum(xs) / len(xs)


def formatuj(wartosc, precyzja=2, jednostka=""):
    tekst = f"{wartosc:.{precyzja}f}"
    if jednostka:
        return f"{tekst} {jednostka}"
    return tekst


def raport(nazwa, *pomiary, **opcje):
    # Przekazujemy 'pomiary' bez gwiazdki, bo 'srednia' przyjmuje jedną sekwencję
    s = srednia(pomiary)
    return f"{nazwa}: {formatuj(s, **opcje)}"

dane = [8,12,10]

print(srednia(dane))

print(raport("Temperatura", 8, 12, 10, precyzja=1, jednostka="°C"))

print(raport("Ciśnienie", *dane, precyzja=0, jednostka="hPa"))