# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo: ').upper().split()

print('O seu nome tem Silva?:', 'SILVA' in nome)