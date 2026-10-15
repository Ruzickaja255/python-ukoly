a=int(input("Zadej a: "))
b=int(input("Zadej b: "))
c=int(input("Zadej c: "))

if a > b:
    d=a
    a=b
    b=d

if b > c:
    d=b
    b=c
    c=d

if a > b:
    d=a
    a=b
    b=d

print(f"a= {a}, b= {b}, c= {c}")