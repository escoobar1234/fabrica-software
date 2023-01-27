pao = float(input("digite a quantidade  a quantidade de pães vendidos "))
broa = float(input("digite a quantidade  a quantidade de broas vendidas "))

q_pao = (pao * 1)

q_broas = (broa * 3.50)

lucros = (q_pao + q_broas)

poup = (lucros * 10 / 100)

print("* pães............................................... %s R$" % q_pao)
print("* broas..............................................%d r$ " % q_broas)
print("* lucros............................................%2.f R$ " % lucros)
print("* poupança............................................. %s R$ " % poup)
