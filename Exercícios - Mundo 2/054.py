from datetime import date
x = date.today().year
b = 0
c = 0

for y in range(0, 7):
    z = int(input('Digite seu ano de nascimento:'))
    a = x - z
    if a >= 21:
        b += 1
    else:
        c += 1
print('Parabéns, {} pessoa(s) já pode(m) ser presa(s)!'.format(b))
print('Olá para o(s) {} bebezinho(s)!'.format(c))
