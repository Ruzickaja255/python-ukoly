import math

#KONTROLA PRVOČÍSLA

print("Kontrola prvočísla")
cislo = int (input("Zadej celé číslo: "))
je_prvocislo=True

if cislo<2:
    je_prvocislo=False
elif cislo==2:
    je_prvocislo=True
elif cislo%2==0:
    je_prvocislo=False
else:
    delitel=3
    while delitel<=math.sqrt(cislo):
        if cislo%delitel==0:
            je_prvocislo=False
            break
        delitel+=2

if je_prvocislo:
    print(f"Číslo {cislo} je prvočíslem.")
else:
    print(f"Číslo {cislo} není prvočíslem.")