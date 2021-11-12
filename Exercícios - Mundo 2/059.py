print('')
a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
print('''
=====MENU OPERACIONAL=====
Digite os números entre os colchetes para
a reaização das seguintes operações:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')
c = int(input('Operação desejada:'))
while c != 5:
    if c == 1:
        d = a + b
        print(f'{a} + {b} = {d}.')
        c = int(input('Operação desejada:'))
    if c == 2:
        e = a * b
        print(f'{a} x {b} = {e}.')
        c = int(input('Operação desejada:'))
    if c == 3:
        if a == b:
            print('Os números apresentam o mesmo valor.')
        elif a > b:
            print(f'O número {a} é o maior.')
        else:
            print(f'O número {b} é o maior.')
        c = int(input('Operação desejada:'))
    if c == 4:
        a = float(input('Novo número:'))
        b = float(input('O outro novo número:'))
        c = int(input('Operação desejada:'))
    else:
        print('Opção Inválida!')
if c == 5:
    print('Muito obrigado!')
