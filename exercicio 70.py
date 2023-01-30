nome = input("digite o nome do atleta:")
salto = float(input("digite a altura do salto:"))
maior = salto
menor = salto
cont = 0
soma = 0
soma = salto + 1
while cont < 4:
    salto = float(input("digite a altura do salto:"))
    if salto < menor:
        menor = salto
    elif salto > maior:
        maior = salto
    soma = soma + salto
    cont = cont + 1
print(f"O melhor salto foi:{maior}")
print(f"O pior salto foi :{menor}")
print(f"A media dos saltos foi:{soma/5:.2f} ")
print("resultado final:")
print(f"{nome}:{soma/5:.2f}")
