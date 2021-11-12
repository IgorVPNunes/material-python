import datetime

x = int(input('Digite o seu ano de nascimento:'))
y = datetime.date.today().year
z = y - x
b = 18 - z
a = z - 18

if z > 18:
    print('Você deveria ter se alistado a {} anos.'.format(a))
elif z == 18:
    print('Você deverá se alistar esse ano.')
else:
    print('Você deverá se alistar daqui a {} anos.'.format(b))
