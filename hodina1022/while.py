# vek=int(input("Zadejte váš věk: "))
# if vek<18:
#    print("Jste nezletilý.")

vek=int(input("Zadejte váš věk: "))
while vek<18 and vek>=0:
    print("Jste nezletilý.")
    vek=int(input("Opakujte zadání věku (ukončím zápornou hodnotou): "))
if (vek>=18):
    print("Přístup povolen.")
else:
    print("Přístup není povolen.")