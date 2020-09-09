# -*- coding: utf-8 -*-
caminho = input("Digite o caminho do arquivo a ser aberto: ")

try:
    arq = open(caminho, "r")
    print("Arquivo aberto com sucesso! O conteudo do arquivo é:")
    print(arq.read())
except:
    print("Erro, caminho inválido!")

