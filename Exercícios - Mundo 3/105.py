def notas(* n, sit=False):
    """
    ~> Função para anaizar as notas de alunos.
    :param n: notas que se desejam registrar.
    :param sit: indica se a situação está boa, ruim ou mediana.
    :return: dicionário com as informações.
    """
    dic = {}
    media = 0
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    for a in n:
        media += a
    m = media / len(n)
    dic['média'] = m
    if sit:
        if m < 6:
            dic['situação'] = 'RUIM'
        elif m <= 7:
            dic['situação'] = 'BOA'
        else:
            dic['situação'] = 'MEDIANA'
    return dic


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
