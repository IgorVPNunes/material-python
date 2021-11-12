from random import choice
from time import sleep
num = []
rand = list(range(0, 11))


def sorteio():
    for a in range(0, 5):
        b = choice(rand)
        num.append(b)


def somaPar():
    x = 0
    for b in num:
        if b % 2 == 0:
            x += b
    print(f'Somando os valores pares  de {num}, temos {x}.')


sorteio()
print('Sorteando 5 valores da lista: ')
for c in num:
    print(c, end=' ')
    sleep(1)
print('PRONTO!')
somaPar()
