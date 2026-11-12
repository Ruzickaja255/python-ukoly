# Výpočet celkové výměry (v m2) bytu

# definice funkce pro výpočet obsahu obdelníku
def obsah_obdelnika(a, b):
    if a<=0 or b<=0:
        return None
    obsah = a * b
    return obsah

# Hlavní tělo programu

print("Výpočet celkové výměry bytu")
print("******************************")

pocet_mistnosti = int(input("Zadej počet místností v bytě: "))
mistnost = 1 # číslo místnosti
celkova_vymetra = 0

while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. místnosti")
    strana_a = int(input("Zadej rozměr 'a' v metrech: "))
    strana_b = int(input("Zadej rozměr 'b' v metrech: "))
    obsah =obsah_obdelnika(strana_a, strana_b)
    if obsah != None:
        # přičtení obsahu místnosti k celkové výměry bytu
        celkova_vymetra += obsah

    mistnost += 1
else:
    print("Chybné zadání místnosti!")

print(f"Celková výměra bytu je {celkova_vymetra} m2.")