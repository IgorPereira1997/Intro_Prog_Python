# -*- coding: utf-8 -*-

def isFloat(n):
    try:
        float(n)
        return True
    except:
        return False

def baskara(a, b, c, delta ,op):
    if(op == "+"):
        return ((b*(-1) + (delta**(1/2)))/(2*a))
    else:
        return ((b*(-1) - (delta**(1/2)))/(2*a))

def complexPartBaskara(a, delta):
        return (delta**(1/2))/(2*a)



flag = True
a = 0
b = 0
c = 0

print("\n")
while(flag):
    aux1 = input('Digite o termo "a" de ax² + bx + c = 0: ')
    if isFloat(aux1):
        a = float(aux1)
        if a != 0:
            flag = False
        else:
            print('Valor igual a 0, invalida equação de segundo grau, tente novamente!\n')
    else:
        print('Valor inválido, tente novamente!\n')

while(not(flag)):
    aux1 = input('Digite o termo "b" de ax² + bx + c = 0: ')
    if isFloat(aux1):
        b = float(aux1)
        flag = True
    else:
        print('Valor inválido, tente novamente!\n')

while(flag):
    aux1 = input('Digite o termo "c" de ax² + bx + c = 0: ')
    if isFloat(aux1):
        c = float(aux1)
        flag = False
    else:
        print('Valor inválido, tente novamente!\n')

delta = (b**2) - (4*a*c)
result1 = 0
result2 = 0

if(delta > 0):
    result1 = baskara(a, b, c, delta, "+")
    result2 = baskara(a, b, c, delta, "-")
elif delta == 0:
    result1 = result2 = baskara(a, b, c, delta, "+")
else:
    result1 = complex((b*(-1))/(2*a), complexPartBaskara(a, -delta))
    result2 = complex((b*(-1))/(2*a), -complexPartBaskara(a, -delta))

print(("\nx1 = {:.2f} e x2 = {:.2f}\n").format(result1, result2))
