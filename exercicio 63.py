num = int(input("digite um numero:"))
menor = num
maior = num
soma = 0
while num != -1:
    soma = soma + num
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
    num = int(input("digite outro numero"))
print(f"o menor é: {menor}")
print(f"o maior é:{maior}")
print(f"a soma dos numeros digitados é:{soma}")