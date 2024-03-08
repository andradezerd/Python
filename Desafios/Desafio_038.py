# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('\nDigite seu PRIMEIRO número: '))
num2 = int(input('\nDigite seu SEGUNDO número: '))

if num1 > num2:
    print (f'O {num1} é MAIOR que {num2}')
elif num2 > num1:
    print (f'O {num2} é MAIOR que {num1}')
else:
    print (f'Os números {num1} e {num2} são iguais')