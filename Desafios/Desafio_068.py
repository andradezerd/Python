# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitoria = 0

print ('\n')
print ('=-' * 12)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('=-' * 12)

while True:
    jogador_num = int(input('\nDigite um valor: '))
    computador_num = randint(0,10)
    total = jogador_num + computador_num
    jogador_esc = ' '
    while jogador_esc not in 'PI':
        jogador_esc = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
        print ('=-' * 12)
    print (f'''JOGADOR escolheu {jogador_num}
COMPUTADOR escolheu {computador_num} 
VALOR TOTAL é de {total}''')
    print ('=-' * 12)
    if jogador_esc == 'P':
        if total % 2 == 0:
            print ('>>> Você VENCEU! <<<')
            vitoria += 1
        else:
            print ('>>> Você PERDEU! <<<')
            break
    elif jogador_esc == 'I':
        if total % 2 == 1:
            print ('>>> Você VENCEU! <<<')
            vitoria +- 1
        else:
            print ('>>> Você PERDEU! <<<')
            break
        print ('Vamos jogar novamente...')
print ('\n')
print (f'\nGAME OVER! Você venceu {vitoria} vezes')
print ('\n')
print ('\n')

