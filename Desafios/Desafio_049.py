# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

valor = int(input('\nDigite seu número inteiro: '))

for c in range (1,11):
    print(f'{valor} x {c} = {valor*c}')
