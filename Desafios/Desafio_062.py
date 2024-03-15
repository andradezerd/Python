# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print ('\nGerador de PROGRESSÃO ARITMÉTICA')
print ('-=' * 16)
primeiro =  int(input('\nDigite o primeiro termo da PA: '))
razao =  int(input('Digite a razão da PA: '))
termo = primeiro
count = 1
total = 0
novos_termos = 10

while novos_termos != 0:
    total += novos_termos
    while count <= total:
        print (f'{termo} -> ', end='')
        termo += razao
        count += 1
    print ('PAUSA')
    novos_termos = int(input('Quantos termos você quer mostrar mais? '))
print (f'\nPROGRESSÃO FINALIZA! {total} termos foram mostrados')



