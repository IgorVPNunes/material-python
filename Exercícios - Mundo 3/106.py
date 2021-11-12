def titulo():
    print('\033[31m~\033[m'*60)
    print('\033[31mSISTEMA DE AJUDA PyHELP\033[m'.center(65))
    print('\033[31m~\033[m'*60)


def manual(y):
    print('\033[32m~\033[m'*60)
    print(f'\033[32mAcessando o manua do comando "{y}"\033[m'.center(65))
    print('\033[32m~\033[m'*60)


def helpsist():
    titulo()
    a = input('Função ou biblioteca: ').lower()
    if a == 'fim':
        print('\033[36m~\033[m' * 60)
        print('\033[36mATÉ LOGO!\033[m'.center(65))
        print('\033[36m~\033[m' * 60)
        return
    manual(a)
    print(help(a))
    while a != 'fim':
        return helpsist()


helpsist()
