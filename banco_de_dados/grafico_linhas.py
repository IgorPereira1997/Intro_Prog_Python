
import matplotlib.pyplot as plt

titulo = "Scatterplot: gráfico de dispersão"
# titulo = "Gráfico de barras 2"
eixox= "Eixo X"
eixoy = "Eixo Y"

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]
z = [200, 25, 400, 3300, 100]

# Legenda
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# plt.bar(x1, y1, label = "Grupo 1")
# plt.bar(x2, y2, label = "Grupo 2")
# plt.legend()

plt.scatter(x1, y1, label = "Meus pontos", 
            color = "#000000", marker="h", s = z)
plt.plot(x1, y1, color="k", linestyle = "--")
plt.legend()

#plt.show()
plt.savefig("figura1.png", dpi=300)

'''
Matplotlib - documentação
Documentação oficial do Matplotlib
A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).



color: cor (ver exemplos abaixo)

label: rótulo

linestyle: estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker: marcador (ver exemplos abaixo)



CORES (color)
'b' blue

'g' green

'r' red

'c' cyan

'm' magenta

'y' yellow

'k' black

'w' white



Marcadores (marker)
'.' point marker

',' pixel marker

'o' circle marker

'v' triangle_down marker

'^' triangle_up marker

'<' triangle_left marker

'>' triangle_right marker

'1' tri_down marker

'2' tri_up marker

'3' tri_left marker

'4' tri_right marker

's' square marker

'p' pentagon marker

'*' star marker

'h' hexagon1 marker

'H' hexagon2 marker

'+' plus marker

'x' x marker

'D' diamond marker

'd' thin_diamond marker

'|' vline marker

'_' hline marker
'''
