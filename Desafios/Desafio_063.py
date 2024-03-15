# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print ('\n')
print ('-'*32)
print ('>>>> Sequência de Fibonacci <<<<')
print ('-'*32)

num = int(input('Quantos termos deseja mostrar? '))
termo1 = 0
termo2 = 1

print ('-'*32)
print (f'{termo1} -> {termo2}', end='')
contador = 3
while contador <= num:
    termo3 = termo1 + termo2
    print (f' -> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
