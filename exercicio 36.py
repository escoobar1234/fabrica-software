print("Cachorro Quente       100")
print("Ovo Simples           101")
print("Bauru com Ovo         102")
print("Hambúrguer            103")
print("Refrigerante          201")
print("Suco                  202")
print("Água Mineral          203")
lanche = float(input("digite o codigo do lanche"))
bebida = float(input("digite o codigo da bebida"))

if (lanche == 100):
    lanche = 11.20

if (lanche == 101):
    lanche = 8.30

if (lanche == 102):
    lanche = 11.30

if (lanche == 103):
    lanche = 16.20

if (bebida == 201):
    bebida = 6.0

if (bebida == 202):
    bebida = 7.50

if (bebida == 203):
    bebida = 4.70

p_t = (lanche + bebida)

print("* lanche............................................... %s R$" % lanche)
print("* bebida................................................%d r$ " % bebida)
print("* preço..................................................%2.f R$ " % p_t)
