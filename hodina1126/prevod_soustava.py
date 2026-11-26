def cifra_na_znak(hodnota):
    if hodnota >= 0 and hodnota <= 9:
        return str(hodnota)
    elif hodnota == 10:
        return "A"
    elif hodnota == 11:
        return "B"
    elif hodnota == 12:
        return "C"
    elif hodnota == 13:
        return "D"
    elif hodnota == 14:
        return "E"
    elif hodnota == 15:
        return "F"

def preved_soustavu(cislo, zaklad):
    if cislo < 0:
        return None
    if zaklad != 2 and zaklad != 8 and zaklad != 10 and zaklad != 16:
        return None
    if cislo == 0:
        return 0

zaklad = 16
cislo = 253
vysledek= ""
while cislo > 0:
    zbytek = cislo % zaklad
    cislo = cislo // zaklad
    vysledek = str(zbytek) + vysledek

print(vysledek)
