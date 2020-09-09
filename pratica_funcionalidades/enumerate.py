# funcao enumarate

lista = ["Abacate", "Bola", "Perfume"]

for i in range(len(lista)):
    print(i, lista[i])

print("\n\n")

lista = ["Abacate", "Bola", "Perfume"]
for i, nome in enumerate(lista):
    print(i, nome)