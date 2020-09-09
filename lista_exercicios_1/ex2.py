# -*- coding: utf-8 -*-

def isFloat(n):
    try:
        float(n)
        return True
    except:
        return False


flag = True
nota1 = 0
nota2 = 0

while(flag):
    aux1 = input('Digite a primeira nota a ser analisada: ')
    if isFloat(aux1):
        nota1 = float(aux1)
        if (nota1 >=0) and (nota1 <=10):
            flag = False
        else:
            print('Nota inválida, tente novamente!\n')
    else:
        print('Valor inválido, tente novamente!\n')

while(not(flag)):
    aux2 = input('Digite a segunda nota a ser analisada: ')
    if isFloat(aux2):
        nota2 = float(aux2)
        if (nota2 >= 0) and (nota2 <= 10):
            flag = True
        else:
            print('Nota inválida, tente novamente!\n')
    else:
        print('Valor inválido, tente novamente!\n')

media = (nota1 + nota2) /2
if(media >= 6):
    print("Aluno está aprovado!")
else:
    print("Aluno está reporvado!")
