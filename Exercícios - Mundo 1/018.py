import math

x = float(input('Digite o valor de um ângulo:'))

s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))

print('Desse ângulo podemos dizer que: Seu seno vale {:.2f}\nSeu cosseno vale {:.2f}\nSua tangente vale {:.2f}'.format(s,c,t))
