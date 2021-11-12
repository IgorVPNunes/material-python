from random import choice
print('')
print('Tente acertar o número escolhido pelo computador (de 0 a 10)!')
a = list(range(0, 11))
b = choice(a)
c = int(input('Seu palpite:'))
d = 1
while b != c:
    c = int(input('Tente de novo:'))
    d += 1
print(f'Parabéns! O número escolhido foi {b} e você acertou com {d} tentativas!')
