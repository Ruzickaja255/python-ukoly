pocet_mesicu = int(input("Zadejte počet měsíců simulace: "))
a=1
b=1
mesic=1

while mesic <= pocet_mesicu:
    print(f"Měsíc {mesic}: {a} pár(ů) | {'🐇' * a}")

    dopredu = a + b
    a = b
    b = dopredu
    mesic += 1
    
print (f"Na císařském ostrově bude po {pocet_mesicu} měsících celkem {b - a} párů králíků.")