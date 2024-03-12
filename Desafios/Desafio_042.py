# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

reta1 = float(input('\nDigite o comprimento da PRIMEIRA reta: '))
reta2 = float(input('Digite o comprimento da SEGUNDA reta: '))
reta3 = float(input('Digite o comprimento da TERCEIRA reta: ')) 

triangulo = reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2

if triangulo == True:
    print('\nÉ um triângulo! E é um triângulo ',end='')
    if reta1 != reta2 and reta2 != reta3 and reta3 !=reta1:
        print('ESCALENO, pois todos lados são diferentes.')
    elif reta1 == reta2 == reta3:
        print ('EQUILÁTERO, pois todos os lados são iguais.')
    else:
        print ('ISÓSCELES, pois dois lados são iguais e um é diferente.')

else:
    print('\nNão é um triângulo')