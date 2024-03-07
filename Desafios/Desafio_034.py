# Escreva um programa que pergunte o salário de um funcionário 
# E calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('\nDigite o seu salário: '))

if salario > 1250:
    aumento = salario * 0.10
    print (f'\nSeu novo salário é {salario + aumento}\nCom um aumento de {aumento}')
else:
    aumento = salario * 0.15
    print (f'\nSeu novo salário é {salario + aumento}\nCom um aumento de {aumento}')