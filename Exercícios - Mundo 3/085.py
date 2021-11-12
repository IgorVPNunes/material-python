td = []
par = []
impar = []
for a in range(0, 7):
    num = int(input(f'Digite um número inteiro para a posição {a + 1}: '))
    td.append(num)
    if td[a] % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
print('='*40)
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')
