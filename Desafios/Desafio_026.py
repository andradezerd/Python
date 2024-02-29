# Faça um programa que leia uma frase pelo teclado 
# e mostre quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez 
# e em que posição ela aparece a última vez.

frase = str(input('\nDigite uma frase: ')).strip().lower()

print('\nQuantidade de vezes que a letra ''a'' aparece:', frase.count('a'))

print('Em que posição o a aparece a primeira vez:',(frase.find('a')+1))

print('Em que posição o a aparece pela ultima vez:',(frase.rfind('a')+1))