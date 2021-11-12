x = int(input('Digite um número  inteiro de 0 a 9999:'))

m = (x // 1000) % 10
c = (x // 100) % 10
d = (x // 10) % 10
u = (x // 1) % 10

print('Unidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}'.format(u, d, c, m))
