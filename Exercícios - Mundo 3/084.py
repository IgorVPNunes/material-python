tot = []
pes = []
peso = []
while True:
    print('='*20)
    n = str(input('Digite seu nome: '))
    p = float(input('Digite seu peso: '))
    peso.append(p)
    print('='*20)
    fim = str(input('Deseja continuar? [s/n]: '))
    pes.append(n)
    pes.append(p)
    tot.append(pes[:])
    a = max(peso)
    b = min(peso)
    pes.clear()
    if fim in 'Nn':
        break
num = len(tot)
print('='*30)
print(f'O número de pessoas cadastradas foi {num}.')
print(f'O maior peso foi {a}Kg e as pessoas com esse peso foram: ', end='')
for c, d in enumerate(peso):
    if d == a:
        print(f'{tot[c][0]} ', end='')
print(f'\nO menor peso foi {b}Kg e as pessoas com esse peso foram: ', end='')
for c, d in enumerate(peso):
    if d == b:
        print(f'{tot[c][0]} ', end='')
print('\n')
print('='*30)
