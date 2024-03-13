# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro =  int(input('\nDigite o primeiro termo da PA: '))
razao =  int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao

print('\nOs dez primeiros termos da razão são: ')
for c in range (primeiro, decimo + razao, razao):
    print(f' {c}', end=' ➡️ ')
print (' ACABOU!')