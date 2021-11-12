print('='*20)
print('Desenvolvendo uma PA')
print('='*20)
a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão da PA: '))
c = a
d = 1
while d <= 10:
    print(f'{a}', end=' -> ')
    a += b
    d +=1
print('Fim')
