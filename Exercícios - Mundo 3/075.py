d = ()
g = ()
e = f = 0
for a in range(0, 4):
    b = int(input('Digite um número inteiro: '))
    c = tuple(str(b))
    d += c
    if '9' in d:
        e = d.count('9')
    if '3' in d:
        f = d.index('3')

    if b % 2 == 0:
        g += c
print('')
print(f'O valor 9 apareceu {e} vezes.')
if '3' in d:
    print(f'O primeiro valor 3 apareceu, pela primeira vez, na posição {f + 1}.')
else:
    print(f'O primeiro valor 3 não apareceu.')
print(f'Os números pares foram: {g}')
