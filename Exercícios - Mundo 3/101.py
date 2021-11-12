from datetime import date


def voto(ano):
    at = date.today().year
    idade = at - ano
    if idade < 16:
        print(f'Seu voto foi negado porque você tem {idade} anos.')
    elif idade in (16, 17) or idade >= 70:
        print(f'Seu voto é opcional pois você tem {idade} anos.')
    else:
        print(f'Seu voto é obrigatório pois você tem {idade} anos.')


nasc = int(input('Digite o ano de seu nascimento: '))
voto(nasc)
