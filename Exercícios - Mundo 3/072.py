a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
b = 0
c = list(range(21))
while True:
    b = int(input('\nDigite um número de 0 a 20: '))
    if b not in c:
        print('Número não válido, tente novamente.')
    else:
        print(a[b])
        d = input('Deseja continuar? [S/N]: ').upper()
        if d == 'N':
            print('FIM')
            break
