x = int(input('Digite em número inteiro:'))
z = 0
for y in range(2, x):
    if x % y == 0:
        z += 1
if z == 0 and x != 1:
    print('Esse é um número primo.')
if x == 1:
    print('Esse número não é primo.')
else:
    print(f'Esse número tem {z} divisores além do 1 e dele mesmo.')
