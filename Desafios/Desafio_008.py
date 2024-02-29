# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valor =  float(input('\nInsira seu valor em METROS: '))
centi = (valor * 100)
mili  = (valor * 1000)

print (f'Seu VALOR: {valor}\nEm CENTÍMETROS: {centi}\nEm MILÍMETROS: {mili}')
