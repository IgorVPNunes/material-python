a = {}
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
a['nome'] = nome
a['media'] = media

if media >= 7:
    a['situação'] = 'Aprovado'
else:
    a['situação'] = 'Reprovado'

print('')
print(f'O nome é igual a {a["nome"]}')
print(f'A média é igual a {a["media"]}')
print(f'A situação é igual a {a["situação"]}')
