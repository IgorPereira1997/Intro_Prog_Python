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


validOp = ['+', '-', '*', '/']
op = ""
expressao = []

print("\n-----------YO SOY UNA CALCULADORA v1.0----------\n")
for i in range(0, 3):
    flag = True
    perg = "Digite o {:d}° número: ".format(i+1)
    while(flag):
        if i == 1:
            op = input("Type the operation (choose between '*', '/', '+', '-'): ")
            if op in validOp:
                expressao.append(op)
                flag = False
            else:
                print("Operação inválida, try again!\n")
        else:
            aux = input(perg)
            if isInt(aux):
                expressao.append(int(aux))
                flag = False
            elif isFloat(aux):
                expressao.append(float(aux))
                flag = False
            else:
                print("Número inválido, try again!\n")

print("\n-----------YO SOY UNA CALCULADORA v1.0----------\n")

if op == "+":
    expressao.append(expressao[0]+expressao[2])
elif op == "-":
    expressao.append(expressao[0]-expressao[2])
elif op == "*":
    expressao.append(expressao[0]*expressao[2])
elif op == "/":
    expressao.append(expressao[0]/expressao[2])

resposta = "{:.2f} ".format(expressao[0]) + expressao[1] + " {:.2f} = {:.2f}".format(expressao[2], expressao[3])
print(resposta,"\n\n")