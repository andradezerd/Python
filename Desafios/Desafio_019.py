# Um professor quer sortear um dos seus quatro alunos para pagar o quadro
# Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido

import random

print ('VAMOS SORTEAR UM DOS SEUS QUATRO ALUNOS')

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice (alunos)

print ('Seu aluno sorteado foi:', sorteado)