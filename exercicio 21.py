salario = float(input("digite o seu salario"))
vendas = float(input("digite o valor de suas vendas"))

comissao = (vendas*0.04)
print(f"a comissão das vendas é  {comissao}")

salario_final = (salario + comissao)

print(f"o salario final é  {salario_final}")