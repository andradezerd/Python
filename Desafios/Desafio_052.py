# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('\n\033[mDigite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print ('\033[33m', end='')
        tot += 1
    else:
        print ('\033[31m',  end='')
    print (f'{c} ', end='')
print (f'\n\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print ('E por isso ele \033[32m É PRIMO!\n\033')
else: 
    print ('E por isso ele \033[31mNÃO É PRIMO!\n\033')