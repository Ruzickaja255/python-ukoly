#vstupy
den=input("Zadejte den představení: ")
mnozstvi=int(input("Kolik osob?: "))
student=input("Jste student? [ano/ne]: ")
vek=int(input("Zadejte váš věk: "))

#vyhodnoceni typu vstupenky
cena_zaklad=500
nazev_slevy= ""

if den=="sobota" or den=="neděle":
    cena_zaklad=cena_zaklad+50
if mnozstvi>=4:     #pravidlo které má vyšší prioritu než věk
    cena_celkem=mnozstvi*cena_zaklad*0.75
    nazev_slevy= "Sleva pro skupiny"
else:               #věková pravila (student nebo senior)
    if vek<26 and student=="ano":
        cena_celkem=mnozstvi*cena_zaklad*0.7
        nazev_slevy= "Sleva pro studenty"
    elif vek>=65:
        cena_celkem=mnozstvi*cena_zaklad*0.8
        nazev_slevy= "Sleva pro seniory"
    else:
        cena_celkem=mnozstvi*cena_zaklad



#Výstupy
print("-------------Výsledná účtenka-------------")
print("Cena celkem je:", cena_celkem, "Kč")
if nazev_slevy!="":
    print(nazev_slevy)

if mnozstvi==1:
    print(f"{mnozstvi} osoba")
elif mnozstvi==2 or mnozstvi==3 or mnozstvi==4:
    print(f"{mnozstvi} osoby")
else:
    print(f"{mnozstvi} osob")

