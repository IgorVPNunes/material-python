import random

w = str(input('Digite o nome de um(a) aluna(o):'))
x = str(input('Digite o nome de um(a) segundo aluna(o):'))
y = str(input('Digite o nome de um(a) terceiro aluna(o):'))
z = str(input('Digite o nome da(o) útima(o):'))

r = [w, x, y, z]
a = random.choice(r)

print('{} foi a pessoa escolhida para ir apagar o quadro.'.format(a))
