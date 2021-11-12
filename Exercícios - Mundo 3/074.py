from random import randint

a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for b in a:
    print(b, end=' ')
print(f'\nO maior valor é {max(a)}.')
print(f'O meno valor é {min(a)}.')

'''
MEU JEITO

from random import randint

print('Os números sorteados foram:', end=' ')
c = 10
d = 0
for a in range(0, 5):
    b = randint(0, 10)
    print(f'{b}', end=' ')
    if b < c:
        c = b
    elif b > d:
        d = b

print(f'\nO menor número é {c}.')
print(f'O maior número é {d}.')
'''