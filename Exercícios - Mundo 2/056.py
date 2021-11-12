b = 0
d = 0
e = 0
f = 0
for a in range(1, 5):
    print(f'=Pessoa {a}=')
    x = str(input('Digite seu nome:')).strip()
    y = int(input('Agora sua idade:'))
    b += y
    z = int(input('Para terminar, seu sexo.\n(1 para Masculino e 2 para feminino):'))
    print('')
    if a == 1 and z == 1:
        d = z
        e = z
    if z == 1 and y > d:
        d = y
        e = x
    if z == 2:
        if y > 20:
            f += 1
c = b / 4
print(f'A média de idade do grupo é de {c} ano(s).')
print(f'O nome do homem mais velho é {e}.')
print(f'O número de mulheres que tem menos de 20 anos é {f}.')
