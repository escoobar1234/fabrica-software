print("*"*41)
print("*"*10,"1-pizza R$35.00      ","*"*10)
print("*"*10,"2-lasanha R$30.00    ","*"*10)
print("*"*10,"3-macarão R$25.00    ","*"*10)
print("*"*10,"4-refrigerante R$4.00","*"*10)
print("*"*10,"5-suco R$4.00        ","*"*10)
print("*"*41)
pedido = int(input("escolha o numero de seu pedido"))
gorjeta = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato, 's' ou 'n'")

if pedido == 1 and gorjeta == "s":
    pedido = 35.00
    taxa1 = (pedido * (10 / 100))
    taxa = (pedido + taxa1)
    print(f"o valor a pagar é {taxa:.2f}")
if pedido == 1 and gorjeta == "n":
    print(f"o valor é R$35.00")
if pedido == 2 and gorjeta == 's':
     pedido = 30.00
     taxa1 = (pedido * (10 / 100))
     taxa = (pedido + taxa1)
     print(f"o valor é R${taxa:.2f}")
if pedido == 2 and gorjeta == "n":
    print(f"o valor é R$ 30.00")
if pedido == 3 and gorjeta == 's':
     pedido = 25.00
     taxa1 = (pedido * (10 / 100))
     taxa = (pedido + taxa1)
     print(f"o valor é R${taxa:.2f}")
if pedido == 3 and gorjeta == "n":
    print(f"o valor é R$ 25.00")
if pedido == 4 and gorjeta == 's':
        pedido = 4.00
        taxa1 = (pedido * (10 / 100))
        taxa = (pedido + taxa1)
        print(f"o valor é R${taxa:.2f}")
if pedido == 4 and gorjeta == "n":
        print(f"o valor é R$ 4.00")
if pedido == 5 and gorjeta == 's':
     pedido = 3.50
     taxa1 = (pedido * (10 / 100))
     taxa = (pedido + taxa1)
     print(f"o valor é R${taxa:.2f}")
if pedido == 5 and gorjeta == "n":
    print(f"o valor é R$ 2.50")



