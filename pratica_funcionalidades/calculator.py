# -*- coding: utf-8 -*-
flag = True
validOp = ['+', '-', '*', '/']

print("---------- YO SOY UNA CALCULADORA v1.0----------")
while(flag):
    num = input("Type the first number: ")

    if not(num.isnumeric()):
        print("Not a number, Try again!\n")
    else:
        num1 = int(num)
        flag = False

while(not(flag)):
    op = input("Type the operation (choose between '*', '/', '+', '-'): ")
    if op in validOp:
        flag = True
    else:
        print("Invalid operation, try again!\n")

while(flag):
    num = input("Type the second number: ")

    if not(num.isnumeric()):
        print("Not a number, Try again!\n")
    else:
        num2=int(num)
        flag = False

if flag and op=="+":
    result = num1+num2
    print(num1," ", op," ", num2, " = ", result)
elif op == "-":
    result = num1-num2
    print(num1," ", op," ", num2, " = ", result)
elif op == "*":
    result = num1*num2
    print(num1," ", op," ", num2, " = ", result)
elif op =="/":
    result = num1/num2
    print(num1, " ", op, " ", num2, " = ", result)
