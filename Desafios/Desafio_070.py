# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

tot_gasto = qtd_produtos1000 = menor = contador = 0
nome_barato = ' '

while True:
    produto_nome = str(input('\nDigite o NOME do produto: '))
    produto_valor = float(input('Digite o PREÇO do produto: R$'))
    contador += 1
    tot_gasto += produto_valor
    if produto_valor >= 1000:
        qtd_produtos1000 += 1
    if contador == 1 or produto_valor < menor:
        menor = produto_valor
        nome_barato = produto_nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print (f'''\nTotal Gasto: R${tot_gasto:.2f}
Quantidade de produtos acima de R$1000: {qtd_produtos1000} produtos
Produto mais barato: {nome_barato} 
Custo do mais barato: R${menor:.2f}
''')
    