# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print ('\n>>>> Contar e Somar <<<<')

num = contador = soma = 0

while num != 999:
    num = int(input('''Digite um número inteiro
Para parar utilize [999]: '''))
    contador += 1
    soma += num
print (f'\nVocê digitou {contador-1} números e a soma entre eles foi de {soma-999}')