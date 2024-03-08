# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor_produto = float(input('\nDigite o PREÇO NORMAL do produto: R$'))

dinheiro_cheque = valor_produto - (valor_produto * 10/100)
cartao_a_vista = valor_produto - (valor_produto * 5/100)
cartao_2x = valor_produto
cartao_3x = valor_produto + (valor_produto *20/100)


print ('''\nFormas de Pagamento: 
[ 1 ]  À vista dinheiro/cheque
[ 2 ]  À vista no cartão
[ 3 ]  Em até 2x no cartão
[ 4 ]  3x ou mais no cartão
''')

metodo = int(input('Método de Pagamento escolhido: '))

if metodo == 1:
    print (f'\nO valor do produto é R${dinheiro_cheque:.2f}')
elif metodo == 2:
    print (f'\nO valor do produto é R${cartao_a_vista:.2f}')
elif metodo == 3:
    print (f'\nO valor do produto é R${cartao_2x:.2f}')
elif metodo == 4:
    print (f'\nO valor do produto é R${cartao_3x:.2f}')