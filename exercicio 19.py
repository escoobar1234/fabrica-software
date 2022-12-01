a = float(input("digite o tamanho do lado 1"))
b = float(input("digite o tamanho do lado 2"))
c = float(input("digite o tamanho do lado 3"))

if  (a + b > c ) and (a + c > b) and (b + c > a):
   print ("formam um triangulo")


if (a == b) and (b == c):
    print ("triangulo equilatero")

if (a == b and a == c and b == c):
    print ("triangulo isósceles")

else:
    print ("triangulo escaleno")