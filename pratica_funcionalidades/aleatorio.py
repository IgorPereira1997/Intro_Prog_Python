import random as r
import math as m

print(m.ceil(r.random()*10))

print(r.randint(0,10))

numeros = [1, 56, 14, 67, 129, 4, 35, 7, 2, 90]
result = r.choice(numeros)
print(result)