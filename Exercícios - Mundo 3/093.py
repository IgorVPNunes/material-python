td = {}
gols = []
total = 0
part = 1
nome = str(input('Digite o nome do jogador: '))
td['nome'] = nome
num = int(input(f'Quantas partidas {nome.title()} jogou? '))
for a in range(0, num):
    tot = int(input(f'Quantos gols ele fez na partida {a + 1}? '))
    gols.append(tot)
    total += tot
td['gols'] = gols
td['total'] = total
print('='*40)
print(f'O nome do jogador é {td["nome"]}.')
print(f'A sequencia de gols dele foi {td["gols"]}.')
print(f'O número total de gols dele foi {td["total"]}')
print('='*30)
print(f'O jogador {nome} jogou {num} partidas.')
for c in gols:
    print(f'     -> Na partida {part}, fez {c} gols.')
    part += 1
print(f'Foi um total de {td["total"]} gols.')
