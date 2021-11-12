td = [[], [], []]
s1 = s2 = 0
for a in range(0, 3):
    for b in range(0, 3):
        num = int(input(f'Digite um número para a posição {a, b}: '))
        td[a].append(num)
        if num % 2 == 0:
            s1 += num
print('\n', '='*30)
for c in range(0, 3):
    print('')
    s2 += td[c][2]
    for d in range(0, 3):
        print(f'[ {td[c][d]} ]', end='')
maior = max(td[1])
print('\n', '='*30)
print(f'A soma de todos os valores pares é {s1}.')
print(f'A soma dos valores da terceira coluna é {s2}.')
print(f'O maior valor da segunda linha é {maior}.')
