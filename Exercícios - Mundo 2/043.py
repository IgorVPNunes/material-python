print('Irei calcular seu IMC')
print(' ')

x = float(input('Digite seu peso (em Kg):'))
y = float(input('Digite sua altura (em m)'))

z = x / (y * y)

if z > 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(z))
elif 18 >= z > 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.'.format(z))
elif 25 >= z > 30:
    print('Seu IMC é {:.2f} e você está acima do peso.'.format(z))
elif 30 >= z > 40:
    print('Seu IMC é {:.2f} e você está obeso.'.format(z))
else:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida.'.format(z))
