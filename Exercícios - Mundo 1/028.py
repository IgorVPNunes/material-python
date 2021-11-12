import random

print('O programa irá sortear um número de 0 a 5 para você tentar acertar!')

a = [0, 1, 2, 3, 4, 5]
b = random.choice(a)

x = int(input('Seu chute:'))

if x == b:
    print('Boa, você acertou! PARABÉNS!')
else:
    print('Puts... não foi dessa vez. TENTE DE NOVO!')
