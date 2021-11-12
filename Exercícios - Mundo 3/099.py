from time import sleep


def lin():
    print('~'*40)
    print('Analizando os valores passados', end='')
    for a in range(0, 3):
        print('.', end='')
        sleep(1)
    print('')


def maior(* x):
    for b in x:
        print(f'{b} ', end='')
    print(f'- Foram informados {len(x)} valores ao todo.')
    if len(x) == 0:
        c = 0
        print(f'O maior valor informado foi {c}.')
    else:
        print(f'O maior valor informado foi {max(x)}.')


lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()
