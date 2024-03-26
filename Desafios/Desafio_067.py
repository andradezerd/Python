# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite o número que deseja ver a tabuada: '))
    if num < 0:
        break
    print ('-' * 45)
    for cont in range(1, 11):
        print (f'{num} x {cont} = {num*cont}')
    print ('-' * 45)
print ('\nNúmeros negativos não são permitidos. PROGRAMA ENCERRADO!')