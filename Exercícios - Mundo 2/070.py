d = e = f = g = 0
h = ' '
while True:
    print('-'*30)
    a = str(input('Digite o nome do produto: '))
    b = float(input('Digite o preço do produto: R$'))
    g += 1
    c = ' '
    while c not in 'SN':
        c = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()
    print('-'*30)
    d += b
    if b > 1000:
        e += 1
    if g == 1:
        f = b
        h = a
    else:
        if b < f:
            f = b
            h = a
    if c == 'N':
        print(f'O valor total gasto foi R${d:.2f}.')
        print(f'{e} produtos custaram mais de R$1000.00.')
        print(f'O produto mais barato se chama {h} e custou R${f:.2f}.')
        print('-'*30)
        break
