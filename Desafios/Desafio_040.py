# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('\nDigite sua PRIMEIRA nota: '))
nota2 = float(input('\nDigite sua SEGUNDA nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print ('\nMédia abaixo de 5.0: REPROVADO')
elif media > 7.0:
    print ('\nMédia 7.0 ou superior: APROVADO')
else:
    print ('\nMédia entre 5.0 e 6.9: RECUPERAÇÃO')

