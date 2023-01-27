nasci = int(input("digite o seu ano de nascimento"))
ano = int(input("digite o ano atual"))

idade = (ano - nasci)
print(f"sua idade é {idade}")

meses = (idade * 12)
print(f"sua idade em meses é {meses}")

semanas = (idade * 52)
print(f"sua idade em semanas é {semanas}")

dias = (idade * 365)
print(f"sua idade em dias é {dias}")
