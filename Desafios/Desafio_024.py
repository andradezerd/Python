# Crie um programa que leia o nome de uma cidade 
# e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('\nDigite o nome de sua cidade: ')).strip().lower().capitalize()

print ('Santo' in cidade[:5])