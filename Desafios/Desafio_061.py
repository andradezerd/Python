# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print ('\nGerador de PROGRESSÃO ARITMÉTICA')
print ('-=' * 16)
primeiro =  int(input('\nDigite o primeiro termo da PA: '))
razao =  int(input('Digite a razão da PA: '))
termo = primeiro
count = 1

while count <= 10:
    print (f'{termo} -> ', end='')
    termo += razao
    count += 1
print ('Fim')
