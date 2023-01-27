salario = float(input("digite o valor do salario"))

if salario <= 280 :
    salario_atual = salario+(salario*0.2)
    print(f"o aumento do salario foi de 20%, seu novo salário é de {salario_atual}")

if salario > 280 and salario <=700:
    salario_atual = salario+(salario*0.15)
    print(f"o aumento do salario foi de 15%, seu novo salário é de {salario_atual} ")

if salario > 700 and salario <=1500:
   salario_atual = salario+(salario*0.1)
   print(f"o aumento do salario foi de 10%, seu novo salario é de {salario_atual} ")

if salario > 1500:
   salario_atual = salario+(salario*0.05)
   print(f"o aumento do salario foi de 5%< seu salario é de {salario_atual}")