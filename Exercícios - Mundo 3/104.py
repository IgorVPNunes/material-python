def leiaint():
    x = input('Digite um número: ')
    while not x.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        x = input('Digite um número: ')
    else:
        print(f'\033[32mVocê acabou de digitar o número {x}.\033[m')


leiaint()
