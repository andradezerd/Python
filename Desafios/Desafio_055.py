# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for pessoas in range (1, 6):
    peso = float(input(f'\nDigite o peso da {pessoas}° pessoa: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'\nO MAIOR peso lido foi de {maior} KG')
print (f'\nO MENOR peso lido foi de {menor} KG')
