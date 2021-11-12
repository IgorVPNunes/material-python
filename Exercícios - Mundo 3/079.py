a = []
while True:
    print('='*30)
    b = int(input('Digite um número inteiro: '))
    if b not in a:
        a.append(b)
        print('Adicionado com sucesso!')
    else:
        print('Esse número já foi adicionado anteriormente.')
    c = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print('='*30)
    if c == 'N':
        break
print(f'Você digitou os valores {a.sort()}')
