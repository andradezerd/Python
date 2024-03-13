 # Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0 
nome_homem_velho = ''
tot_mulher20 = 0

for pessoas in range (1, 5):
    print (f' ======> {pessoas}° PESSOA <======')
    nome = str(input(f'\nDigite o NOME: ')).strip()
    idade = int(input(f'\nDigite a IDADE: '))
    sexo = str(input(f'\nDigite o SEXO [M ou F]: ')).strip()
    soma_idade += idade

    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

media_idade= soma_idade / 4
print (f'\nA média de idade das quatro pessoas é de {media_idade}')
print (f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_velho}')
print (f'E são {tot_mulher20} mulheres que tem menos de 20 anos')
