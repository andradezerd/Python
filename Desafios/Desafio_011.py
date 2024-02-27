# Faça um programa que leia a largura e a altura de uma parede em metros
# Calcule a sua área e a quantidade de tinta necessária para pintá-la 
# Sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Qual a LARGURA da sua parede em METROS? '))
altura = float(input('Qual a ALTURA da sua parede em METROS'))
area = (largura * altura)
tinta = (area / 2)

print (f'Você vai precisar de {tinta} litros de tinta')


