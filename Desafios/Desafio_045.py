# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

jokenpo = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print ('''\n>>> VAMOS JOGAR JOKENPÔ !!! <<<
\nDIGITE SE VAI QUERER PEDRA, PAPEL OU TESOURA
[ 0 ]  Pedra
[ 1 ]  Papel
[ 2 ]  Tesoura''')

jogador = int(input('\nQual é a sua jogada? '))

print (' ')
print ('-=' *12)
print (f'Computador jogou {jokenpo[computador]}')
print (f'Jogador jogou {jokenpo[jogador]}')
print ('-=' *12)
print (' ')

if computador == 0: 
    if jogador == 0:
        print ('\033[0;30;47mEMPATE\033[m')
    elif jogador == 1:
        print ('\033[0;30;46mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print ('\033[0;30;41mCOMPUTADOR VENCE\033[m')
    else:
        print ('Jogada inválida')

elif computador == 1: 
    if jogador == 0:
        print ('\033[0;30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print ('\033[0;30;47mEMPATE\033[m')
    elif jogador == 2:
        print('\033[0;30;46mJOGADOR VENCE\033[m')
    else:
        print ('Jogada inválida')

elif computador == 2: 
    if jogador == 0:
        print ('\033[0;30;46mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print ('\033[0;30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print ('\033[0;30;47mEMPATE\033[m')
    else:
        print ('Jogada inválida')

