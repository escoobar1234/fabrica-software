peso = int(input("Entre com o peso: "))

if peso > 50:
	excesso = peso - 50
	multa   = excesso * 4
else:
	excesso = 0
	multa = 0


print(
    f"\npeso        : {peso:.2f}",
    f"\nexcesso     : {excesso:.2f}kg",
    f"\nmulta       : R${multa:.2f}",
    )
