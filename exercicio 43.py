um = int(input("digite a quantidade de moedas de 1 centavo:"))
dois = int(input("digite a quantidade de moedas de 5 centavos:"))
tres = int(input("digite a quantidade de moedas de 10 centavos:"))
quatro = int(input("digite a quantidade de moedas de 25 centavos:"))
cinco = int(input("digite a quantidade de moedas de 50 centavos:"))
seis = int(input("digite a quantidade de moedas de 1 real:"))

umC = (um * 1) / 100
print(f"um centavo:R${umC:.2f}")
cincoC = (dois * 10) / 100
print(f"cinco centavos:R${cincoC:.2f}")
dezC = (tres * 10) / 100
print(f"dez centavos:R${dezC:.2f}")
vintecincoC = (quatro * 25) / 100
print(f"vinte e cinco centavos:R${vintecincoC:.2f}")
cinquentaC = (cinco * 50) / 100
print(f"cinquenta centavos:R${cinquentaC:.2f}")
umR = (seis * 1)
print(f"um real:R${umR:.2f}")
total = (umC + cincoC + vintecincoC + cinquentaC + umR)
print(f"o total economizado é R${total:.2f}")