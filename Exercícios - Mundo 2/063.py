a = int(input('Digite um número inteiro:'))
b = 0
c = 1
print(f'{b} -> {c}', end='')
e = 3
while e <= a:
    d = b + c
    print(f' -> {d}', end='')
    b = c
    c = d
    e += 1
print(' -> FIM')
