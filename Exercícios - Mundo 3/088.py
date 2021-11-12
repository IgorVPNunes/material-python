from time import sleep
from random import choice
c = list(range(1, 60))
print('='*30)
print('JOGO DA MEGA-SENA'.center(30))
print('='*30)
a = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(0.5)
print('='*30)
print(F' SORTEANDO {a} JOGOS'.center(30))
print('='*30)
sleep(1)
for b in range(0, a):
    print(f'Jogo {b + 1}: {choice(c), choice(c), choice(c), choice(c), choice(c), choice(c)}')
    sleep(0.5)
print('='*30)
print('BOA SORTE'.center(30))
print('='*30)
