print('='*20)
print('Desenvolvendo uma PA')
print('='*20)
x = int(input('Digite o primeiro termo:'))
y = int(input('Digite a razão da PA:'))
a = x + (10 - 1) * y
for z in range(x, a + y, y):
    print('{}'.format(z), end=' - ')
print('Fim')
