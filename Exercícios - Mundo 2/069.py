d = e = f = 0
while True:
    print('-'*30)
    a = int(input('Digite sua idade: '))
    if a > 18:
        d += 1
    b = ' '
    while b not in 'MF':
        b = str(input('Agora seu sexo [M/F]: ')).upper().strip()
    if b == 'M':
        e += 1
    c = ' '
    while c not in 'sn':
        c = str(input('Deseja continuar [s/n]: ')).lower().strip()
    if b == 'F' and a < 20:
        f += 1
    if c == 'n':
        print('-'*30)
        print('Ok, muito obrigado')
        print(f'O número de pessoas com idade acima de 18 é {d}.')
        print(f'O número de homens cadastrados foi {e}.')
        print(f'O número de mulheres com menos de 20 anos é {f}.')
        print('-'*30)
        break
