szam1 = float(input("Adj meg egy számot: "))
szam2 = float(input("Adj meg egy másik számot: "))

osszeg=szam1+szam2
print("A két megadott szám összege: ", osszeg)


szam = int(input("Adj meg egy számot: "))
if szam % 2 == 0:
    print("A megadott szám páros")
else:
    print("A megadott szám páratlan")


szam1 = float(input("Adj meg egy számot: "))
szam2 = float(input("Adj meg egy második számot: "))
szam3 = float(input("Adj meg egy harmadik számot: "))
if szam1 > szam2 and szam3:
    print("A legnagyobb szám:", szam1)
elif szam2 > szam1 and szam3:
    print("A legnagyobb szám:", szam2)
else:
    print("A legnagyobb szám:", szam3)