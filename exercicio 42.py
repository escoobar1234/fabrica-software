lata = int(input("digite a guantidade de latas compradas:"))
garrafa = int(input("digite a quantidade de garrafas de 600 ml compradas:"))
garrafa1 = int(input("digite a quantidade de garrafas de 2 l compradas :"))

l = (lata * 350) / 1000
print(f"Latas de 350 ml: {l} L")

g = (garrafa * 600) / 1000
print(f"Garrafas de 600 ml :{g} L")

g1 = (garrafa1 * 2)
print(f"Garrafas de 2 litros: {g1} L ")

total = (l + g + g1)
print(f"total em litros : {total} L")