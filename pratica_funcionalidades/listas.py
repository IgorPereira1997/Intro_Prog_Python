#-*- coding: utf-8 -*-

frutas = ["abacaxi", "melancia", "avocado"]

print(len(frutas))

# add items to the list
frutas.append("strawberry")

#verify if an item is on the list
try:
    print(frutas.index("banana"))
except:
    print("'banana' is not on the list!")

#delete list
del(frutas)

numeros = [1, 56, 14, 67, 129, 4, 35, 7, 2, 90]


#sort items
numeros.sort()
# reverse sort ==> numeros.sort(reverse=True)

#inverse list ==> numeros.inverse()
numeros = sorted(numeros)
print(numeros)


