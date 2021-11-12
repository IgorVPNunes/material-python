import random

print('JOGO JOQUEMPÔ')

a = ('Pedra', 'Papel', 'Tesoura')

x = input('Sua jogada:')
z = x.title()
y = random.choice(a)

if z == y:
    print('EMPATE!')
if z == 'Pedra' and y == 'Papel':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você PERDEU!')
if z == 'Pedra' and y == 'Tesoura':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você GANHOU!')
if z == 'Papel' and y == 'Pedra':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você GANHOU!')
if z == 'Papel' and y == 'Tesoura':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você PERDEU!')
if z == 'Tesoura' and y == 'Pedra':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você PERDEU!')
if z == 'Tesoura' and y == 'Papel':
    print('Você escolheu {} e o computador escolheu {}'.format(z, y))
    print('Você GANHOU!')
