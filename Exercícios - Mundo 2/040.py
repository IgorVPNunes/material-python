x = float(input('Digite uma nota de avaiação:'))
y = float(input('Digite uma outra nota:'))

z = (x + y) / 2

if z < 5:
    print('Sua média foi {:.1f}, então você foi REPROVADO!'.format(z))
elif 5 <= z < 7:
    print('Sua média foi {:.1f}, entao você está de RECUPERAÇÃO!'.format(z))
else:
    print('Sua média foi {:.1f}, entao você foi APROVADO!'.format(z))
