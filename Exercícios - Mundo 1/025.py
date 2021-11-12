x = input('Digite seu nome completo:')

a = x.title()
b = a.strip()
c = b.split()
d = 'Silva' in c

print('Você tem o sobrenome Silva?:{}'.format(d))
