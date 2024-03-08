# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float (input('\nDigite seu peso: '))
altura = float (input('\nDigite sua altura: '))

imc = (peso / (altura ** 2))

print (f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print ('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print ('Parabéns, você está no PESO IDEAL')
elif 25 <= imc < 30:
    print ('Você está em estado de SOBREPESO')
elif 30 <= imc < 40:
    print ('\nVocê está em estado de OBESIDADE')
else:
    print ('CUIDADO! Você está em estado de OBESIDADE MÓRBIDA')


