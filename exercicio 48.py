preco = float(input("digite o preço do produto"))
paga = input("digite 'p' para pix, 'c' para cartão")

if paga == "p":
    desc = (preco * (10 / 100))
    preco1 = (preco - desc)
    print(f"R${preco1:.2f}")

if paga == "c":
    parce = int(input("digite em quantas vezes sera a compra"))
    if parce == 1:
        desc = (preco * (5 / 100))
        preco1 = (preco - desc)
        print(f"R${preco1:.2f}")
    if parce == 2:
        print(f"R${preco:.2f}")
    if parce == 3:
        juros = (preco * (10 / 100))
        preco1 = (preco + juros)
        print(f"R${preco1:.2f}")

