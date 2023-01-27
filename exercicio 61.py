num = int(input("digite um numero"))
contador = 1
impar = 0
par = 0
while contador < 10:
    contador = contador + 1
    if num % 2 == 1:
        impar += 1
    else:
        par += 1
    num = int(input("digite um numero"))

print(f"A quantidade de numeros impares foram: {impar}")
print(f"A quantidade de numeros pares foram: {par}")


