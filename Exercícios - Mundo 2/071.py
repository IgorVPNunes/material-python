print('='*30)
print('             BANCO BOT            ')
print('='*30)
while True:
    a = int(input('Qua valor deseja sacar?: R$'))
    b = a // 50
    c = a - (50 * b)
    d = c // 20
    e = c - (20 * d)
    f = e // 10
    g = e - (10 * f)
    h = g // 1
    print('')
    print(f'{b} notas de 50.\n{d} notas de 20.\n{f} notas de 10.\n{h} notas de 1.')
    break
