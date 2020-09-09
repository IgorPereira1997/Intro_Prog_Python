# -*- coding: utf-8 -*-

op = 0

while(op != 3):
    print("\n-----------MENU DE OPÇÕES------------\n")
    print("-----------1 - Ler arquivo-----------")
    print("-2 - Imprimir conteudo de um arquivo-")
    print("--------------3 - Sair---------------")
    aux = input("Opção: ")
    print("-------------------------------------\n")
    if aux.isnumeric():
        op = int(aux)
        if op == 1:
            caminho = input("Digite o caminho do arquivo a ser aberto: ")
            try:
                arq = open(caminho, "r")
                print("Arquivo aberto com sucesso!")
            except:
                print("Erro, caminho inválido!")
        
        elif op == 2:
            print("O conteudo do arquivo é:")
            print(arq.read())
            
        elif op == 3:
            print("Obrigado por utilizar o programa!")
            arq.close()
        else:
            print("Erro, valor inválido digitado!")
