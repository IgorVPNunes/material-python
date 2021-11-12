from math import sqrt

print('Digite o tamanho de três retas.')
x = int(input('Reta um:'))
y = int(input('Reta dois:'))
z = int(input('Reta três:'))

a = sqrt((y - z) ** 2)
b = sqrt((x - z) ** 2)
c = sqrt((x - y) ** 2)

if a < x < y + z and b < y < x + z and c < z < x + y:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
