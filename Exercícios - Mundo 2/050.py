print('Digite 6 números inteiros')
z = 0
for x in range(0, 6):
    y = int(input('Número:'))
    if y % 2 == 0:
        z += y
print(f'A soma dos números pares é {z}.')
