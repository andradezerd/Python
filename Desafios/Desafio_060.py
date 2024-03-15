# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('\nDigite o NÚMERO para calcular seu Fatorial: '))
count = num
fatorial = 1

print (f'\nCalculando {num}! = ', end='')

while count > 0:
    print (f'{count} ', end='')
    print ('x ' if count > 1 else '= ', end='')
    fatorial *= count
    count -= 1
print (f'{fatorial}')
