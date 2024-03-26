# Crie um programa que leia vários números inteiros pelo teclado,
# E no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quantidade = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('\nDigite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print (f'\nVocê digitou {quantidade} números sendo a média entre eles {media}!')
print (f'MAIOR valor: {maior}\nMENOR valor: {menor}')