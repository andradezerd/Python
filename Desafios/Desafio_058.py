# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# Mostrando no final quantos palpites foram necessários para vencer.

import random

num = random.randint(0, 10)
tot_tentativas = 1

print ('\n>>>>>>>>> VAMOS JOGAR UM JOGO <<<<<<<<<\nEu, seu COMPUTADOR, escolhi um NÚMERO ENTRE 0 e 10!\nTENTE DESCOBRIR QUAL É!')
num_escolhido = int(input('\nPALPITE do JOGADOR: '))

while num_escolhido != num:
    num_escolhido = int(input('ERROU! Esse não é o número do COMPUTADOR, tente novamente até acertar: '))
    tot_tentativas += 1
    
print (f'\nPARABÉNS!!!\nVocê ganhou do COMPUTADOR após {tot_tentativas} tentativas!')
