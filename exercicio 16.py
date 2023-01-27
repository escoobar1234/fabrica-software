n1 = int(input("digite o primeiro numero"))
n2 = int(input("digite o segundo numero"))
n3 = int(input("digite o terceiro numero"))

if n1 < n2 and n1 < n3 :
    print(f"{n1} é menor que {n2} e {n3}")

if n1 > n2 and n1 > n3:
    print(f"{n1} é maior do que {n2} e {n3}")

if n2 < n1 and n2 < n3:
   print(f"{n2} é menor do que {n1} e {n3} ")

if n2 > n1 and n2 > n3:
    print(f"{n2} é maior do que {n1} e {n3}")

if n3 < n1 and n3 < n2 :
    print(f"{n3} é menor que {n2} e {n1}")

if n3 > n1 and n3 > n2:
    print(f"{n3} é maior do que {n2} e {n1}")