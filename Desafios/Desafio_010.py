# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considerando a cotação do Dólar do dia 27/02/2024 que é 4,94

carteira = float(input('\nQuanto dinheiro você tem na carteira? '))
dolar = float(4.94)
conversao = round((carteira / dolar),2)

print (f'Você pode comprar R${conversao} com esse dinheiro')
