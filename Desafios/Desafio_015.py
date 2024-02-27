# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# E a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

alugadokm = float(input('Quantos KMs foram percorridos com o carro alugado? '))
alugadodias = int(input('Quantos DIAS ficou com o carro alugado? '))

precokm = alugadokm * 0.15
precodias =  alugadodias * 60

alugadopreco = precokm + precodias

print (f'Seu VALOR TOTAL a pagar pelo aluguel do carro é de: R${alugadopreco:.2f}')
print (f'R${precodias} pelos DIAS alugados')
print (f'R${precokm} pela QUILOMETRAGEM percorridas ')

