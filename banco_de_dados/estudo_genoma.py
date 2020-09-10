entrada = open("16s_bacteria.fasta").read()
saida = open("16s_bacteria.html", "w")

entrada2 = open("18s_humano.fasta").read()
saida2 = open("18s_humano.html", "w")

cont = {}
cont2 = {}

for i in ["A", "T", "C", "G"]:
    for j in ["A", "T", "C", "G"]:
        cont[i+j] = 0
        cont2[i+j] = 0

entrada = entrada.replace("\n", "")
entrada2 = entrada2.replace("\n","")

for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1
    cont2[entrada2[k] + entrada2[k+1]] += 1

# html

i = 1
for k in cont:
    alpha = cont[k]/max(cont.values())
    alpha2 = cont2[k]/max(cont2.values())
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; color: aqua; background-color: rgba(0, 0, 0,"+ str(alpha) +" )'>"+ k +"</div>")
    saida2.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; color: aqua; background-color: rgba(0, 0, 0," + str(alpha2) + " )'>"+ k +"</div>")
    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
        saida2.write("<div style='clear:both'></div>")
    i += 1

saida.close()
saida2.close()
