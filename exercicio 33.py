num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
op = input("Digite a operação que deseja realizar: [+, -, /, *]: ")
if op == "+":
    result = num1 + num2
    print(f"o resultado é:{result}")
if op == "-":
    result = num1 - num2
    print(f"o resultado é:{result}")
if op == "*":
    result = num1 * num2
    print(f"o resultado é:{result}")
if op == "/":
    result = num1 / num2
    print(f"o resultado é:{result}")
if result %2==0:
    print("o resultado da soma é par")
else:
    print("o resultado da soma é impar")
if result > 0:
    print(f"o resultado da soma é positivo")
else:
    print("o resultado da soma é negativo")
if (result == round(result)):
    print("o resultado da soma é inteiro")
else:
    print(f"{result } é um numero decimal")
