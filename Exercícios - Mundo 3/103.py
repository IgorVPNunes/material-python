def ficha(n='', g=''):
    if g == '':
        g = 0
    if n == '':
        n = '<Desconhecido>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


a = str(input('Nome do jogador: '))
b = str(input('Número de gols: '))
ficha(a, b)
