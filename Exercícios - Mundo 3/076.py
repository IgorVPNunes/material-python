a = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila',
     120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('='*33)
print(f'{"LISTAGENM DE PREÇOS".center(33)}')
print('='*33)

for b in range(0, len(a)):
     if b % 2 == 0:
          print(f'{a[b]:.<24}', end='')
     if b % 2 == 1:
          print(f'R$ {a[b]:>6}')
print('='*33)
