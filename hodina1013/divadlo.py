#vstupy
vek=int(input("Zadejte váš věk: "))
student=input("Jste student? [ano/ne]: ")
mnozstvi=int(input("Kolik osob?: "))
den=input("Zadejte den představení: ")


#vyhodnoceni typu vstupenky
cena_zaklad=500
nazev_slevy= ""
priplatek = 50 if (den == "sobota" or den == "neděle") else 0
typ_vztupenky= "(Víkendové představení)" if (den == "sobota" or den == "neděle") else ""

if mnozstvi>=4:     #pravidlo které má vyšší prioritu než věk
    cena_celkem=mnozstvi*(cena_zaklad*0.75)
    nazev_slevy= "Sleva pro skupiny (25%)"
else:               #věková pravila (student nebo senior)
    if vek<26 and student=="ano":
        cena_celkem=mnozstvi*cena_zaklad*0.7
        nazev_slevy= "Sleva pro studenty (30%)"
    elif vek>=65:
        cena_celkem=mnozstvi*cena_zaklad*0.8
        nazev_slevy= "Sleva pro seniory (20%)"
    else:
        cena_celkem=mnozstvi*cena_zaklad



#Výstupy
print("")
print("-------------Výsledná účtenka-------------")

if mnozstvi==1:
    print(f"Typ lístku: {mnozstvi} osoba {typ_vztupenky}")
elif mnozstvi==2 or mnozstvi==3 or mnozstvi==4:
    print(f"Typ lístku: {mnozstvi} osoby {typ_vztupenky}")
else:
    print(f"Typ lístku: {mnozstvi} osob {typ_vztupenky}")

if nazev_slevy!="":
    print("Druh slevy:", nazev_slevy)

print ("Cena za jednu vstupenku je:", cena_celkem/mnozstvi, "Kč")

print("Cena celkem je:", cena_celkem+priplatek, "Kč")
