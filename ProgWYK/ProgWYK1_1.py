#Wykłady z pytohna listy pętle 

nazwy = ["L1","L2","L3"]
dystanse = [8,12,7]


odczyty = {
    nazwa: x
    for nazwa, x in zip(
        nazwy, dystanse, strict=True
    )   
    if x >= 0
}
bliskie = [
    nazwa for nazwa,x in odczyty.items()
    if x < 10
]
