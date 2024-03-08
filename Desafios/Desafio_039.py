# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year

nascimento = int(input('\nDigite o seu ano de nascimento: '))
idade = atual - nascimento

if idade == 18:
    print ('\nEstá no ano de se alistar')

elif idade < 18:
    saldo = 18 - idade
    print (f'\nVocê não precisa se alistar.\nAinda faltam {saldo} anos para o alistamento.')

elif idade > 18:
    saldo = idade - 18
    print (f'\nVocê já deveria ter se alistado há {saldo} anos')