x = str(input('Digite seu nome completo: '))

a = x.strip()
b = a.title()
c = b.split()
d = c[0]
e = len(c)
f = c[e - 1]

print('Seu primeiro nome é: {}\nSeu último nome é: {}'.format(d, f))
