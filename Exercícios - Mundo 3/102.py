def fatorial(x, show=False):
    """
    -> Calcula o fatorial de um número.
    :param x: Número desejado.
    :param show: (Opcional) Mostrar ou não a conta [True/False].
    :return: O valor do fatorial de um número n.
    """
    if show:
        f = 1
        for a in range(0, x):
            y = x - a
            f *= y
            print(f'{y} x ', end='')
        print(f'= {f}')
    else:
        f = 1
        for a in range(0, x):
            y = x - a
            f *= y
        print(f)


fatorial(5)
