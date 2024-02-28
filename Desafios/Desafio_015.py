# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# E a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

alugado_km = float(input('Quantos KMs foram percorridos com o carro alugado? '))
alugado_dias = int(input('Quantos DIAS ficou com o carro alugado? '))

preco_km = alugado_km * 0.15
preco_dias =  alugado_dias * 60

alugado_preco = preco_km + preco_dias

print (f'Seu VALOR TOTAL a pagar pelo aluguel do carro é de: R${alugado_preco:.2f}')
print (f'R${preco_dias} pelos DIAS alugados')
print (f'R${preco_km} pela QUILOMETRAGEM percorridas ')

