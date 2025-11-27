szam1 = float(input("Adj meg egy számot: "))
szam2 = float(input("Adj meg egy másik számot: "))

osszeg=szam1+szam2
print("A két megadott szám összege: ", osszeg)


szam = int(input("Adj meg egy számot: "))
if szam == 0:
    print("A megadott szám 0, ami se nem páros, se nem páratlan.")
elif szam % 2 == 0:
    print("A megadott szám páros.")
else:
    print("A megadott szám páratlan.")


szam1 = float(input("Adj meg egy számot: "))
szam2 = float(input("Adj meg egy második számot: "))
szam3 = float(input("Adj meg egy harmadik számot: "))

legnagyobb = szam1

if szam2 > legnagyobb:
    legnagyobb = szam2

if szam3 > legnagyobb:
    legnagyobb = szam3

print("A legnagyobb szám:", legnagyobb)

N = int(input("Adj meg egy számot: "))
for i in range (1,N+1):
    print(i)


szamok = []

for i in range(5):
    szam = float(input(f"{i+1}. Adj meg 5 számot: "))
    szamok.append(szam)

print("A megadott számok átlaga:", sum(szamok)/5)