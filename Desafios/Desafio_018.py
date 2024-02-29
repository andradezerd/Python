# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do:
#Seno, Cosseno e Tangente desse ângulo

import math

angulo = float(input('\nInforme um ângulo: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print (f'O SENO do seu ângulo é: {seno:.2f}')
print (f'O COSSENO do seu ângulo é: {cosseno:.2f}')
print (f'O TANGENTE do seu ângulo é: {tangente:.2f}')
