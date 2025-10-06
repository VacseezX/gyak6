import math
gyartasiSzam = int(input("Add meg a csoki gyártási sorszámát: "))
tmp = False
if gyartasiSzam <= 1:
    tmp = False
else:
    tmp = True
    for i in range(2, int(math.sqrt(gyartasiSzam)) + 1):
        if gyartasiSzam % i == 0:
            tmp = False
            break

if tmp != False:
    print("Gratulálok, nyertél!")
else:
    print("Sajnos nem nyert!")