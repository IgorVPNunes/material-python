def lin():
    print('~'*30)


def f():
    print('FIM')


def cont(x, y, z):
    for a in range(x, y, z):
        print(a, end=' ~ ')


lin()
print('De 1 a 10, de 1 em 1')
cont(1, 11, 1)
f()
lin()
print('De 10 a 0, de 2 em 2')
cont(10, -1, -2)
f()
lin()
print('Sua vez!')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
lin()
print(f'De {n1} a {n2}, de {n3} em {n3}.')
if n1 > n2 and n3 < 0:
    cont(n1, n2 - 1, -n3)
elif n3 > 0:
    cont(n1, n2 - 1, n3)
elif n3 < 0:
    n3 *= 1
    cont(n1, n2, n3)
elif n3 == 0:
    cont(n1, n2, 1)
else:
    cont(n1, n2, n3)
f()
