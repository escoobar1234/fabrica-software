A = 80000
B = 200000
taxaA = 0.03
taxaB = 0.015

anos = 0
while A < B:
    A = A + (A * taxaA)
    B = B + (B * taxaB)
    anos = anos + 1

print (f"Serão necessarios {anos} anos para que a população do pais A ultrapasse ou iguale a população do pais B")
print(f"pais A:{A:.0f}   pais B: {B:.0f}")