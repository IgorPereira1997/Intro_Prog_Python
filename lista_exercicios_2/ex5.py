# -*- coding: utf-8 -*-
dicionario = {}
aux = []

caminho = input("Digite o caminho do arquivo a ser aberto: ")
try:
    arq = open(caminho, "r")
    print("Arquivo aberto com sucesso!")
except:
    print("Erro, caminho inválido!")

linhas = arq.readlines()
multifasta = {}

for linha in linhas:
    if linha[0] == ">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] += linha.strip()

for chave in multifasta:
    print("{", chave, ":", multifasta[chave], "}")
