a=float(input("Zadej a: "))
b=float(input("Zadej b: "))
c=float(input("Zadej c: "))

#na zacatu je min i max
min_val=a
max_val=a

#porovnani s b
if b<min_val:
    min_val=b
if b>max_val:
    max_val=b

#porovnani s c
if c<min_val:
    min_val=c
if c>max_val:
    max_val=c

print("minimum je:", min_val)
print("maximum je:", max_val)
