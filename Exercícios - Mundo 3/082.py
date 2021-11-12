a = []
b = []
c = []
while True:
    d = int(input('Digite um número inteiro: '))
    a.append(d)
    if d % 2 == 0:
        b.append(d)
    else:
        c.append(d)
    e = str(input('Deseja continuar? [s/n]')).lower()
    if e == 'n':
        break
print(f'A lista completa é {a}')
print(f'A lista dos números pares é {b}')
print(f'A lista dos números ímpares é {c}')
