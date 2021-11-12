x = input('Digite seu nome completo:')

a = x.upper()
b = x.lower()
z = x.split()
y = ''.join(z)
c = len(y)
d = len(z[0])

print('Todo em maiúsculas:{}\nToda em minúsculas:{}\nQuantas letras ao todo:{}\nQuantas letras no primeiro nome:{}'.format(a, b, c, d))
