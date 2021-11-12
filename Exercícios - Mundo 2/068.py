from random import choice
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-='*10)
print('')
a = True
c = list(range(10))
while a:
    print('-'*30)
    b = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    d = int(input('Digite seu número:'))
    e = choice(c)
    f = e + d
    if f % 2 == 1 and b == 'I':
        print(f'Você escolheu o número {d} e o computador escolheu {e}!')
        print('VOCÊ GANHOU!!')
        print('')
        print('Vamos mais uma vez!')
        a = True
    elif f % 2 == 1 and b == 'P':
        print(f'Você escolheu o número {d} e o computador escolheu {e}!')
        print('VOCÊ PERDEU!!')
        a = False
    elif f % 2 == 0 and b == 'I':
        print(f'Você escolheu o número {d} e o computador escolheu {e}!')
        print('VOCÊ PERDEU!!')
        a = False
    elif f % 2 == 0 and b == 'P':
        print(f'Você escolheu o número {d} e o computador escolheu {e}!')
        print('VOCÊ GANHOU!!')
        print('')
        print('Vamos mais uma vez!')
        a = True
    print('-'*30)
