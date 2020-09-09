# function zip

lista1 = [1 ,2, 3, 4, 5]
lista2 = ["Avocado", "Bola", "Chumacero", "Dog", "Money"]
lista3 = ["R$ 2,00", "R$ 5,00", "R$ 250,00", "R$ 100,00", "R$ 10,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
