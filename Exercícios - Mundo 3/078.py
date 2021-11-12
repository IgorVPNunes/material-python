a = []
for b in range(0, 5):
    a.append(int(input(f'Digite um número inteiro para a posição {b}: ')))
print(f'O maior número digitado foi {max(a)}, na posição ', end='')
for c, d in enumerate(a):
    if d == max(a):
        print(f'{c} ', end='')
print(f'\nO menor número digitado foi {min(a)}, na posição ', end='')
for e, f in enumerate(a):
    if f == min(a):
        print(f'{e} ', end='')
