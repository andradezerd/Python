n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
media = (n1 + n2)/2
print (f'A sua média foi {media:.1f}')
if media >= 6.0:
    print ('Sua me´dia foi boa! PARABÉNS')
else:
    print ('Sua média foi ruim! ESTUDE MAIS')