num = int(input("digite um numero"))
impar = 0
while num != -999:
    if num % 2 == 1:
        impar +=1
    num = int(input("digite um numero"))
print(f"A quantidade de numeros impares foram: {impar}")