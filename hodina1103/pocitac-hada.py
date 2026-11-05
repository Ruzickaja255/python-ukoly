print("Mysli si číslo od 1 do 100 a já se ho pokusím uhodnout.")
print("Odpovídej 'v' - větší, 'm' - menší, 's' - správné")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    pokusy += 1
    tip = (dole + nahore) // 2
    print(f"Myslím si číslo {tip}.")
    odpoved = input("Je to správné? (v/m/s): ")
    
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print(f"Uhádl jsem číslo {tip} na {pokusy} pokusů.")
    else:
        print("Neplatná odpověď, zkus to znovu.")
        pokusy -= 1
