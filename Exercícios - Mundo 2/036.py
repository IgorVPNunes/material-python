print('Boas Vindas ao banco Pyhton!')
x = float(input('Digite o valor da casa que deseja financiar:'))
y = float(input('Agora o valor do seu salário:'))
z = float(input('Para finalizar, em quanto tempo deseja pagar(em meses):'))

a = x / z
b = 0.3 * y

if a <= b:
    print('Você terá que pagar {:.2f} por mês, durante {:.2f} meses.'.format(a, z))
else:
    print('Lamentamos, mas seu pedido de impréstimo foi negado.')
