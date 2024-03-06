# Faça um programa que leia uma frase pelo teclado 
# e mostre quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez 
# e em que posição ela aparece a última vez.

frase = str(input('\nDigite uma frase: ')).strip().lower()

print('\nQuantidade de vezes que a letra "A" aparece:', frase.count('a'))

print('O primeiro "A" aparece na posição:',(frase.find('a')+1))

print('O último "A" aparece na posição',(frase.rfind('a')+1))