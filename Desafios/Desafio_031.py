# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('\nQual distância percorrida da viagem em KMs? '))

if distancia <= 200:
    preco = distancia * 0.50
    print (f'O valor da viagem é de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print (f'O valor da viagem é de R${preco:.2f}')