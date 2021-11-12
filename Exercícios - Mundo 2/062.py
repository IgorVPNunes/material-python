print('='*20)
print('Desenvolvendo uma PA')
print('='*20)
a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão da PA: '))
c = a
d = 1
e = 10
f = 0
while d <= e:
    print(f'{a}', end=' -> ')
    a += b
    d += 1
while f != 'N':
    if e == 10:
        f = str(input('\nVocê deseja ver mais algarismos dessa PA? [S/N]')).upper().strip()
        while f == 'S':
            g = int(input('Mais quantos você deseja ver?'))
            e = e + g
            while d <= e:
                print(f'{a}', end=' -> ')
                a += b
                d += 1
            f = str(input('\nVocê deseja ver mais algarismos dessa PA? [S/N]')).upper().strip()
        if f != 'SN':
            f = str(input('Código Inválido, tente novamente:')).upper().strip()
        elif f == 'N':
            print('OK, muito obrigado.')
print('Fim')
