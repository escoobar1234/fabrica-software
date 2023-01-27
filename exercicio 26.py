v = float(input("digite o preço do produto "))

print(f"o preço do produto é {v}")

if (v < 50):
    lucro = v + (v * 45 / 100)
    print(f"o valor da venda  é {lucro}")

elif (v >= 50 ):
    lucro = v + (v * 30 / 100 )
    print(f"o valor da venda é {lucro}")

