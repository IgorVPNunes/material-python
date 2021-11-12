x = int(input('Digite um número inteiro:'))
y = int(input('Digite outro número inteiro:'))

if x > y:
    print('O primeiro valor é maior ({})'.format(x))
elif x < y:
    print('O segundo valor é maior ({})'.format(y))
else:
    print('Os dois valores são iguais ({} = {})'.format(x, y))
