# O mesmo professor do Desafio_019 quer sortear a ordem de apresentação de trabalho dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle (alunos)

print ('Ordem de apresentação do trabalho:')
print (alunos)
