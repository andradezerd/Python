# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Iorgute', 6.98,
            'Macarrão', 3.58,
            'Manteiga', 20.98,
            'Requeijão', 10.98,
            'Leite em Pó', 15.90,
            'Cereal', 16.98,
            'Biscoito', 2.28,
            'Suco de Uva', 10.98,
            'Maionese', 11.95)
print ('\n')
print ('-' * 38)
print (f'{"LISTAGEM DE PREÇOS":^38}')
print ('-' * 38)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print (f'{listagem[pos]:.<30}', end='')
    else:
        print (f'R${listagem[pos]:>6.2f}')

