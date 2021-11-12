a = 0
b = 0
for x in range(1, 6):
    y = float(input('Digite o peso da pessoa {}:'.format(x)))
    if x == 1:
        a = y
        b = y
    else:
        if y > a:
            a = y
        if y < b:
            b = y
print(f'O maior peso lido foi {a}Kg e o menor peso foi {b}Kg.')