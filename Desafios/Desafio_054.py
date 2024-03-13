# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range (1, 8):
    nasc = int(input(f'\nDigite o {pessoas}° ano de nascimento: '))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print (f'\nAo todo tivemos {totmaior} pessoas maiores de idade')
print (f'E também tivemos {totmenor} pessoas menores de idade')