aluno = 0
totalmulheres = 0
totalhomens = 0
bons = 0
porc = 0

while aluno < 5:

    matricula = int(input("digite sua matricula "))
    sexo = input("digite seu sexo")
    altura = int(input("digite sua altura "))
    status = int(input("1 - bom / 2 - regular / 3 - ruim"))

    if (sexo == "f" and altura > 170):
        totalmulheres = totalmulheres + 1
    else:
        totalhomens = totalhomens + 1

    if (sexo == "m" and status == 1):
        bons = bons + 1
        porc = bons * 100 / totalhomens

    aluno = aluno + 1

print("total de mulheres altas" , totalmulheres)
print("porcentagem de homens bons" , porc)









