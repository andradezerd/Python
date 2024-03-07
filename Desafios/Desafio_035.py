# Desenvolva um programa que leia o comprimento de três retas 
# E diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('\nDigite o comprimento da PRIMEIRA reta: '))
reta2 = float(input('\nDigite o comprimento da SEGUNDA reta: '))
reta3 = float(input('\nDigite o comprimento da TERCEIRA reta: ')) 

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triângulo')
else:
    print('Não é um triângulo')