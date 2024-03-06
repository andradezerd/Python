# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('\nDigite o número que você deseja: '))
resto = num % 2

if resto == 0:
    print ('Seu número é PAR')
else:
    print ('Seu número é ÍMPAR')