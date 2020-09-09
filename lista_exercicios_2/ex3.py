aux = input("Digite a sua sequencia: ")

new_test = open('text1.fasta', "w")

escrever = ">" + aux
new_test.write(escrever)

new_test.close()
