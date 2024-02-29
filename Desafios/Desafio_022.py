# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. 
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('\nDigite seu nome completo: ')
nome_sem_espaco = nome.replace(' ','')
nome_primeiro = nome.split()[0]

print ('Seu nome com todas letras MAIÚSCULAS:',nome.upper())
print ('Seu nome com todas letras MINÚSCULAS:',nome.lower())

print ('Seu nome tem:',len(nome_sem_espaco),'letras')

print ('Seu primeiro nome tem:',len(nome_primeiro),'letras')