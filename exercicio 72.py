nome = input("digite o nome do atleta:")
notas = float(input("digite a nota do atleta:"))
maior = notas
menor = notas
cont = 0
soma = 0
soma = notas + 1
while cont < 6:
    notas = float(input("digite a nota do atleta:"))
    if notas < menor:
        menor = notas
    elif notas > maior:
        maior = notas
    soma = soma + notas
    cont = cont + 1
print(f"O melhor nota foi:{maior}")
print(f"O pior nota foi :{menor}")
print(f"A media das notas foi:{soma/7:.2f} ")
print("resultado final:")
print(f"{nome}:{soma/7:.2f}")
