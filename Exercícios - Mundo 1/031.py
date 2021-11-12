x = int(input('Digite a distância de uma viajem em Km:'))

if x <= 200:
    a = x * 0.5
    print('A passagem custará {:.2f} reais'.format(a))
else:
    b = x * 0.45
    print('A passagem custará {:.2f} reais'.format(b))
