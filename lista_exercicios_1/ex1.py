flag = True
idade = 0

while(flag):
    aux = input('Digite a idade a ser analisada: ')
    if aux.isnumeric():
        idade = int(aux)
        flag = False
    else:
        print('Valor inválido, tente novamente!\n')

if(idade < 18):
    print("Menor de idade!")
else:
    print("Maior de idade!")
