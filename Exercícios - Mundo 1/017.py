import math

x = float(input('Digite o tamanho do cateto adjacente de um triângulo retângulo:'))
y = float(input('Agora do cateto oposto:'))
z = (x.__pow__(2)) + (y.__pow__(2))
h = math.sqrt(z)

print('A hipotenusa desse triângulo retângulo vale {:.2f}.'.format(h))
