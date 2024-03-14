# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('\nDigite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
menu = ('''\nMENU DE ESCOLHAS:
[1] Soma
[2] Multiplicação
[3] Maior / Menor
[4] Escolher novos números
[5] Encerrar o programa''')
escolha = 0 

while escolha != 5:
    print (menu)
    escolha = int(input('\nEscolha uma função entre [1] e [5]: '))
    if escolha == 1:
        somar = num1 + num2
        print (f'\nA soma entre {num1} e {num2} é {somar}')
    elif escolha == 2:
        multiplicar = num1 * num2
        print (f'\nA multiplicação entre {num1} e {num2} é {multiplicar}')
    elif escolha == 3:
        if num1 > num2:
            print (f'\n{num1} é MAIOR do que {num2}')
        elif num2 > num1:
            print (f'\n{num2} é MAIOR do que {num1}')
        else:
            print ('\nOs dois números são idênticos')
    elif escolha == 4:
        novo_num1 = int(input("Novo número 1: \n"))
        novo_num2 = int(input("Novo número 2: \n"))
        num1 = novo_num1
        num2 = novo_num2
        print(menu)
        escolha = int(input("Sua escolha: \n"))
    elif escolha == 5:
        print('\nFinalizando...')
    else: 
        print ('\nOpção inválida. Tente Novamente.')

print ("\nPrograma Encerrado.")