conta = int(input("digite o numero da conta"))
saldo = int(input("digite seu saldo"))
debito = int(input("digite seu débito"))
credito = int(input("digite seu crédito"))

if (saldo - debito + credito) >= 0:
   print("saldo positivo")

else:
    print("saldo negativo")