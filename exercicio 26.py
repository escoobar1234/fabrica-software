v = float(input("digite o preço da venda "))

print(f"o preço do produto é {v}")

if (v <= 50.00):
    lucro = v + (v * 45 / 100)
    print(f"o preco atualizado do produto é {lucro}")

if (v > 50 ):
    lucro = v + (v * 30 / 100 )
    print(f"o preço atualizado do produto é {lucro}")

