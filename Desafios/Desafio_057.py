# Faça um programa que leia o sexo de uma pessoa, 
# Mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('\nInforme qual é o sexo [M ou F]? ')).strip().upper()[0]
    
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe novamente seu sexo: ')).strip().upper()[0]
print (f'Seu sexo foi registrado com sucesso!')