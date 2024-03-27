# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0

while True:
    idade = int(input('\nDigite a IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print (f'''\nTotal de pessoas com mais de 18 anos: {tot18}
Total de homens cadastrados: {totH}
Total de mulheres com menos de 20 anos: {totM20}''')