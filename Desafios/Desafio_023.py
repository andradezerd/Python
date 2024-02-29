# Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.

num = str(input('\nDigite um número de 0 a 9999: ')).zfill(4)

print (f'O número digita foi: {num}')
print (f'Sua unidade é: {num[3]}')
print (f'Sua dezena é: {num[2]}')
print (f'Sua centena é: {num[1]}')
print (f'Seu milhar é: {num[0]}')



