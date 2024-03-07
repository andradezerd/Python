# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)
num_escolhido = int(input('\nDigite um número entre 0 e 5: '))

if num_escolhido == num:
    print (f'\nVOCÊ GANHOU!\nO número sorteado foi o {num}')
else:
    print (f'\nVOCÊ PERDEU!\nO número sorteado foi o {num}')

