#funkce pro vykreslení čtverce
def ctverec(strana):
    radek = 0
    while radek < strana:
        print(strana * "* ")
        radek += 1

#funkce pro vykreslení obdelníka
def obdelník(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
        print(stranaA * "* ")
        radek += 1

#funkce pro vykreslení obdelníka s dírou
def dira(stranaA, stranaB):
    radek = 0
    while radek < stranaB:
         if radek == 0 or radek == stranaB - 1:
            print(stranaA * "* ")
         else:
            print("* " + (stranaA - 2) * "  " + "* ")

print("Kreslím geometrické tvary z hvězdiček.")

pokracovat = True
while pokracovat:
    typ = input ("Jaký obrazec chces vykreslovat?: ")
    if typ == "c":
        ctverec(5)
    elif typ == "o":
        obdelník(3,4)
    elif typ == "on":
        dira(3, 4)
    else:
        print("Musíš určit jeden ze známých tvarů! [c, o]: ")
    odpoved = input("Chceš vykreslit další obrazec? [ano/ne]: ").lower()
    if odpoved != "ano":
        pokracovat = False
