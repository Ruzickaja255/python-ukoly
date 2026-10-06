cas = float(input("Zadejte čas v hodinách: "))
if cas < 0:
    print("Čas není záporný.")
elif cas < 6:
    print("Dobrou noc")
elif cas < 9:
    print("Dobré ráno")
elif cas < 12:
    print("Dobré dopoledne")
elif cas < 18:
    print("Dobrý den")
elif cas < 22:
    print("Dobrý večer")
elif cas <= 24:
    print("Dobrou noc")
else:
    print("Čas není více než 24 hodin.")