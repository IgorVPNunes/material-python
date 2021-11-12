a = int(input('Digite um número inteiro: '))
b = str(input('Deseja continuar? [S/N]: ')).upper().strip()
c = 1
d = a
f = a
g = a
while b != 'N':
    a = int(input('\nDigite um número inteiro: '))
    b = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    c += 1
    d += a
    if a > f:
        f = a
    elif a < g:
        g = a
    else:
        f = g = a
e = d / c
print(f'\nVocê digitou {c} números e a média deles é {e}!')
print(f'O maior valor é {f} e o menor é {g}!')
