def area(x, y):
    a = x * y
    print(f'A largura é {x}m e o comprimento é {y}m, então a área é {a}m2.')


print('CONTROLE DE TERRENOS')
print('='*20)
lar = float(input('Largura (m): '))
com = float(input('Comprimento (m): '))
area(lar, com)
