# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

primeiro = int(input('\nDigite o PRIMEIRO número: '))
segundo = int(input('Digite o SEGUNDO número: '))
terceiro = int(input('Digite o TERCEIRO número: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print('\nMaior:',maior)


menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('\nMenor:',menor)

