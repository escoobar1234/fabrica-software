print("Digite abaixo o numero de sue candidato")
num = int(input("digite: '1'João, '2'Pedro, '3'José,'4'Maria, '5'Nulo, '6'Em Branco "))
soma = 0
soma1 =0
soma2=0
soma3=0
soma4=0
soma5=0
soma6=0
cont = 0
while num != 0:
    soma +=1
    if num == 1 :
        soma1 +=1
    if num == 2 :
        soma2 +=1
    if num == 3 :
        soma3 +=1
    if num == 4 :
        soma4 +=1
    if num == 5 :
        soma5+=1
    if num == 6 :
        soma6 +=1
    num = int(input("digite: '1'joão, '2'pedro, '3'José,'4'Maria, '5'Nulo, '6'Em branco "))
print(f"A quantidade de votos para João é: {soma1}")
print(f"A quantidade de votos para Pedro é: {soma2}")
print(f"A quantidade de votos para José é: {soma3}")
print(f"A quantidade de votos para Maria é: {soma4}")
print(f"A quantidade de votos para Nulo é: {soma5}")
print(f"A quantidade de votos para em Branco é: {soma6}")
print(f"Aporcentagem dos votos nulos é: {(soma5/soma)*100:.2f}%")
print(f"A porcentagem dos votos em branco é: {(soma6/soma)*100:.2f}%")
