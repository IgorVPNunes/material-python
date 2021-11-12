def aumentar(a, a1, x=False):
    e1 = a1 / 100
    e2 = e1 * a
    e3 = a + e2
    if x:
        return f'R${e3:.2f}'.replace('.', ',')
    else:
        return e3


def diminuir(b, b1, x=False):
    f1 = b1 / 100
    f2 = f1 * b
    f3 = b - f2
    if x:
        return f'R${f3:.2f}'.replace('.', ',')
    else:
        return f3


def dobro(c, x=False):
    g = c * 2
    if x:
        return f'R${g:.2f}'.replace('.', ',')
    else:
        return g


def metade(d, x=False):
    h = d / 2
    if x:
        return f'R${h:.2f}'.replace('.', ',')
    else:
        return h


def moeda(i):
    j = f'R${i:.2f}'.replace('.', ',')
    return j


def resumo(k, l, m):
    print('~' * 30)
    print('Resumo do Valor'.center(30))
    print('~' * 30)
    print('Preço analizado:'.ljust(20), end='')
    print(f'R$ {k:.2f}'.rjust(2).replace('.', ','))
    print('Dobro do preço:'.ljust(20), end='')
    print('R$', str(dobro(k)).rjust(2).replace('.', ','))
    print('Metade do preço:'.ljust(20), end='')
    print('R$', str(metade(k)).rjust(2).replace('.', ','))
    print(f'{l}% de aumento:'.ljust(20), end='')
    print('R$', str(aumentar(k, l)).rjust(2).replace('.', ','))
    print(f'{m}% de redução:'.ljust(20), end='')
    print('R$', str(diminuir(k, m)).rjust(2).replace('.', ','))
    print('~' * 30)
