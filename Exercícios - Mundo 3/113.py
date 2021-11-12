def leiaInt():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
        except:
            print('ERRO: Por favor, digite um número válido.')
            continue
        else:
            return a


def leiaFloat():
    while True:
        try:
            b = float(input('Digite um número inteiro: '))
        except:
            print('ERRO: Por favor, digite um número válido.')
            continue
        else:
            return b


leiaInt()
leiaFloat()
