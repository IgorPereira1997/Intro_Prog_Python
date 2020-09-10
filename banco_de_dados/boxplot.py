'''
Boxplot
Boxplot (diagrama de caixa) é uma técnica de visualização de dados em que representa a variação de dados por meio de quartis.
O retângulo central concentra 50% dos dados plotados. A linha ao centro indica a mediana. Os círculos representam os outlines (valores que destoam muito dos outros valores apresentados).


Fonte: próprio autor.

'''

import matplotlib.pyplot as plt
import random
vetor = []

for i in range(10000):
    vetor.append(random.randint(0, 100))

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
