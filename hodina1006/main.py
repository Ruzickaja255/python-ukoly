#polarita proměnné

cislo = float(input("Zadej číslo: "))
if cislo>0:
    print("Kladné číslo")
else:
    if cislo==0:
        print("Nula")
    else:
        print("Záporné číslo")
        cislo = -cislo
print(f"Absolutní hodnota je {cislo}")
if cislo>0:
    print("Kladné číslo")
elif cislo==0:
    print("Nula")
else:
    print("Záporné číslo")
    cislo = -cislo

print(f"Absolutní hodnota je {cislo}")