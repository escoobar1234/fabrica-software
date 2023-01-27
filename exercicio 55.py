num = int(input("digite um numero:"))
menor = num
maior = num

for cont in range(1,5):
    cont += 1
    num = int(input("digite outro numero"))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(f"o menor é: {menor}")
print(f"o maior é:{maior}")

