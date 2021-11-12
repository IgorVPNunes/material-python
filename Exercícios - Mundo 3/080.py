a = []
for b in range(0, 5):
    c = int(input('Digite um número inteiro: '))
    if b == 0 or b > a[-1]:
        a.append(c)
    else:
        d = 0
        while d < len(a):
            if c <= a[d]:
                a.insert(d, c)
                break
            d += 1
print('='*30)
print(f'Os valores digitados, em ordem, foram: {a}')
