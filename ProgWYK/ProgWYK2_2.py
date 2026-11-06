def minmax(*pomiary):
    if not pomiary:
        raise ValueError("Brak pomiarów")
    return min(pomiary), max(pomiary)

wynik1 = minmax(8,12,100)
print(f"minmax(8,12,10) --> {wynik1}")

dane = [3,9,4]
wynik2 = minmax(*dane)
print(f"minmax(*dane) --> {wynik2}")

try:
    minmax()
except ValueError as e:
    print(e)