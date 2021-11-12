print('Digite trên números inteiros diferentes.')
x = int(input('Digite o primeiro número:'))
y = int(input('Digite o segundo número:'))
z = int(input('Digite o terceiro número:'))

if x > y > z:
    print('{} é o maior número e {} é o menor.'.format(x, z))
if x > z > y:
    print('{} é o maior número e {} é o menor.'.format(x, y))
if y > x > z:
    print('{} é o maior número e {} é o menor.'.format(y, z))
if y > z > x:
    print('{} é o maior número e {} é o menor.'.format(y, x))
if z > x > y:
    print('{} é o maior número e {} é o menor.'.format(z, y))
if z > y > x:
    print('{} é o maior número e {} é o menor.'.format(z, x))
