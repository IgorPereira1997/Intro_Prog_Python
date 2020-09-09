# -*- coding: utf-8 -*-

def isFloat(n):
    try:
        float(n)
        return True
    except:
        return False

def isInt(n):
    try:
        int(n)
        return True
    except:
        return False


numeros = []
qtdNum = 0
print("\n")
flag = True

while(flag):
    aux = input("Quantos números serão fornecidos? ==> ")
    if isInt(aux):
        qtdNum = int(aux)
        if qtdNum > 0:
            flag = False
        else:
            print("Número fornecido é inválido, tente novamente!\n")
    else:
        print("Valor fornecido não é um número, tente novamente!\n")

print("\n")

for i in range(0, qtdNum):
    flag = True
    perg = "Digite o termo [{:d}/{:d}] da lista de números: ".format(i+1, qtdNum)
    while(flag):
        aux = input(perg)
        if isInt(aux):
            numeros.append(int(aux))
            flag = False
        elif isFloat(aux):
            numeros.append(float(aux))
            flag = False
        else:
            print('Valor inválido, tente novamente!\n')
    i += 1 

print("\n")
numeros.sort()
print("Os números fornecidos são, organizados de forma crescente: ", numeros)
        
