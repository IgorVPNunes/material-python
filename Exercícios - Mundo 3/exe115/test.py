def leiaInt():
    while True:
        try:
            a = int(input('\033[34mSua opção: \033[m'))
        except:
            print('ERRO: Por favor, digite um número válido.')
            continue
        else:
            return a


def linhas():
    print('-'*40)


def menu(lista):
    linhas()
    print('\033[31mMENU PRINCIPAL\033[m'.center(45))
    linhas()
    c = 1
    for d in lista:
        print(f'\033[32m{c}\033[m - \033[32m{d}\033[m')
        c += 1
    linhas()
    opc = leiaInt()
    return opc


def adicionar():
    addn = str(input('Nome: '))
    lista.append(addn)
    addi = int(input('Idade: '))
    lista.append(addi)
    linhas()
