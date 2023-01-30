nome = input("digite seu nome")

idade = float(input("digite sua idade"))



if (idade>=0) and (idade<=2):

    print(f"{nome} esta com {idade} e pela tabela é considerado um bebe ")

if (idade>=3) and (idade<=11):

    print(f"{nome} esta com {idade} e pela tabela é considerado uma criança ")

if (idade>=12) and (idade<=21):

    print(f"{nome} esta com {idade} e pela tabela é considerado um jovem ")

if (idade>=22) and (idade<=64):

    print(f"{nome} esta com {idade} e pela tabela é considerado um adulto ")

if (idade>=65) and (idade<=100):

    print(f"{nome} esta com {idade} e pela tabela é considerado um idoso ")

if(idade>100):

    print(f"{nome} esta com {idade} e pela tabela é considerado um muito velinho ")
