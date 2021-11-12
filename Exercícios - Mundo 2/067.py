while True:
    a = int(input('Digite um número:'))
    if a < 0:
        break
    b = 1
    print('-' * 30)
    print(f'TABUADA DO {a}')
    while True:
        c = a * b
        print(f'{a} x {b} = {c}')
        b += 1
        if b == 10:
            break
    print('-'*30)
print('-'*30)
print('FIM')