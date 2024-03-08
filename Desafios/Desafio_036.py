# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('\nQual o valor da casa interessada? R$'))
salario = float(input('Qual é o valor do seu salário atual? R$'))
anos_pagar = int(input('Em quantos anos deseja pagar? '))

prestacao = valor_casa / (anos_pagar * 12)
parcela = salario * 30 / 100

print (f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos_pagar} anos a prestação será de R${prestacao:.2f}')

if prestacao > parcela:
    print ('Seu empréstimo foi NEGADO!')
else:
    print ('Seu empréstimo foi APROVADO!')
 