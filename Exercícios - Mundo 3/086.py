td = [[], [], []]
for a in range(0, 3):
    for b in range(0, 3):
        num = int(input(f'Digite um número para a posição {a, b}: '))
        td[a].append(num)

for c in range(0, 3):
    print('')
    for d in range(0, 3):
        print(f'[ {td[c][d]} ]', end='')
