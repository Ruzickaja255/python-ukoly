import urllib.request

url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

# otevření komunikace s webovým serverem, stažení odpovědi ze serveru
odpoved = urllib.request.urlopen(url)

pocet_dnu = 0
celkem_srazek = 0
radek = odpoved.readline()          #čtu první řádek (v Bytech)
while bool(radek):
    text_radku = radek.decode("utf-8")
    srazky = float(text_radku)
    if srazky >= 0:
        celkem_srazek += srazky
        pocet_dnu += 1
    radek = odpoved.readline()      #čtu další řádky
odpoved.close()

print(celkem_srazek / pocet_dnu)