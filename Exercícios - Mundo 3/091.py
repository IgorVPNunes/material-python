from time import sleep
from random import choice
from operator import itemgetter
dicio = {}
win = []
c = 1
a = list(range(0, 6))
print('Valores sorteados:')
for b in range(1, 5):
    dicio[f'jogador{b}'] = choice(a)
    print(f'    O jogador{b} tirou {dicio[f"jogador{b}"]}')
    sleep(1)
print('Ranking dos jogadores:')
win = sorted(dicio.items(), key=itemgetter(1), reverse=True)
for d, e in win:
    print(f'    {c}o. lugar: {d} com {e}')
    c += 1
