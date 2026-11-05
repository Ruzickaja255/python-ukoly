import random

tajne_cislo = random.randint(1, 20)
pokus = 0
tip = 0
max_pokusy = 5

while tip!=tajne_cislo and pokus < max_pokusy:
    tip = int(input("Tipni si cislo od 1 do 20: "))
    pokus += 1
    if tip>tajne_cislo:
        print("Moje číslo je menší.")
    elif tip<tajne_cislo:
        print("Moje číslo je větší.")
else:
    print("Musíš zadávat číslo mezi 1 a 20.")
if tip == tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokus}. pokus.")
else:
    print(f"Bohužel ti došly pokusy! Tajné číslo bylo {tajne_cislo}.")