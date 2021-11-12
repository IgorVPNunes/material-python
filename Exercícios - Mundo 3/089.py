from time import sleep
td = []
alu = [[], []]
extra = 0
while True:
    print('=' * 30)
    nome = str(input('Nome: '))
    alu.insert(0, nome)
    nota1 = float(input('Nota 1: '))
    alu[1].append(nota1)
    nota2 = float(input('Nota 2: '))
    alu[2].append(nota2)
    media = ((nota1 + nota2) / 2)
    alu.append(media)
    td.append(alu[:])
    alu = [[], []]
    print('=' * 30)
    fim = str(input('Deseja continuar? [s/n]: '))
    if fim in 'Nn':
        break

print('\n'*2)
print('='*25)
print('No.   ', end='')
print('NOME', end='')
print('MÉDIA'.rjust(15))
print('-'*25)
for a in range(0, len(td)):
    print(f'{a}'.ljust(6), end='')
    print(f'{td[a][0]}', end='')
    print(f'{td[a][3]}'.rjust(19 - len(td[a][0])))
print('-'*25)
while extra != 999:
    extra = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for a in range(0, len(td)):
        if extra == a:
            print(f'As notas de {td[a][0]} são {td[a][1]} e {td[a][2]}.')
            print('')

print('FINALIZANDO', end='')
for b in range(0, 3):
    print('.', end='')
    sleep(1)
print('\n<<< Volte sempre! >>>')
