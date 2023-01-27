livro = int(input("digite a quntidade de livros comprados no bimestre:"))
if livro == 0:
    pontos = 0
if livro == 1:
    pontos = 5
if livro == 2:
    pontos = 15
if livro == 3:
    pontos = 30
if livro >= 4:
    pontos = 60
print("entre 20 à 30 pontos o cliente poderá escolher entre: Uma Eco Bag OU Caneta personalizada")
print("entre 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira")
print("Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00) OU Power bank")
print("*"*50)
print(f"vc tem {pontos} de pontos.")
