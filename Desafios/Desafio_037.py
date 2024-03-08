# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('\nDigite um número inteiro: '))
          
print ('''\nEscolha a base para sua conversão: 
[ 1 ]  Converter para BINÁRIO
[ 2 ]  Converter para OCTAL
[ 3 ]  Converter para HEXADECIMAL
''')

escolha = int(input('Conversão escolhida: '))

if escolha == 1:
    print (f'{num} em BINÁRIO é: {bin(num)}')

elif escolha ==2:
    print (f'{num} em OCTAL é: {oct(num)}')

elif escolha ==3:
    print (f'{num} em HEXADECIMAL é: {hex(num)}')

else:
    print ('Opção inválida. Tente novamente.')
