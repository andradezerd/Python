# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('\nDigite o seu salário: '))
aumento = (salario * 15)/100+salario

print (f'Seu novo salário com 15% de aumento será R${aumento} !')