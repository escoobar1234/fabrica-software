valor = float(input("Digite o valor da divida:"))

juros1 = valor + (valor * 0.1)
juros2 = valor + (valor * 0.15)
juros3 = valor + (valor * 0.2)
juros4 = valor + (valor * 0.25)

print(f"Valor:       Juros:     Parcelas:       total:")
print(f"{valor:.2f}         0            1          {valor:.2f}")
print(f"{valor:.2f}       {valor*0.1:.2f}         3           {juros1:.2f}")
print(f"{valor:.2f}       {valor*0.15:.2f}         6           {juros2:.2f}")
print(f"{valor:.2f}       {valor*0.2:.2f}         9           {juros3:.2f}")
print(f"{valor:.2f}       {valor*0.25:.2f}        12           {juros4:.2f}")