#8 Choinka z gwiazdek
wysokosc = int(input("Jaką wysoką chcesz choineczkę: "))
for x in range(wysokosc+1):
    print(" "*int(wysokosc-x)+"*"*(2*x-1)+" "*int(wysokosc-x))