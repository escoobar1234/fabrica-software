nome = input("digite seu nome")

disciplina = input("digite o nome da disciplina")

nota = float(input("digite sua primeira nota"))

nota2 = float(input("digite sua segunda nota"))

nota3 = float(input("digite sua terceira nota"))

media = (nota+nota2+nota3)/3
print("a media das notas é: ",media)

if (media > 6):
    print("você foi aprovado")

else:
    print("você foi reprovado")
