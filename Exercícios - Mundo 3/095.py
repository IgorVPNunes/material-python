todos = []
td = {}
gols = []
total = 0
part = 1
while True:
    print('-'*40)
    nome = str(input('Digite o nome do jogador: '))
    td['nome'] = nome
    num = int(input(f'Quantas partidas {nome.title()} jogou? '))
    for a in range(0, num):
        tot = int(input(f'Quantos gols ele fez na partida {a + 1}? '))
        gols.append(tot)
        total += tot
    td['gols'] = gols
    td['total'] = total
    todos.append(td.copy())
    td.clear()
    stop = str(input('Deseja continuar? [s/n]: ')).lower()
    if stop in 'Nn':
        break
print('='*40)
print('Num'.ljust(6), end='')
print('Nome', end='')
print('Gols'.rjust(15), end='')
print('Total'.rjust(15))
print('-'*40)
for b in range(0, len(todos)):
    print(f'{b}'.ljust(6), end='')
    print(f'{todos[b]["nome"]}', end='')
    espace = 15 - len(todos[b]["nome"])
    print(' '*espace, end='')
    print(f'{todos[b]["gols"]}', end='')
    c = 10 - len(todos[b]["gols"])
    print(' '*c, end='')
    print(f'{todos[b]["total"]}')
print()
print('='*40)
