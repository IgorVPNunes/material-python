x = int(input('Digite um número inteiro:'))

print('')

print('''Escolha uma das bases para a conversão.
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')

print('')

y = int(input('Digite a opção:'))

if y == 1:
    print('Esse valor {}, em base binária, fica {}.'.format(x, bin(x)[2:]))

elif y == 2:
    print('Esse valor {}, em base octal, fica {}.'.format(x, oct(x)[2:]))

elif y == 3:
    print('Esse valor {}, em base hexadecimal, fica {}.'.format(x, hex(x)[2:]))

else:
    print('Opção inváida:')
