y = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        y = x + y
print('A soma dos números ímpares e divisiveis por 3 que ficam entre 1 e 500 é {}.'.format(y))
