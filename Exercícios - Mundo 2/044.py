x = float(input('Digite o valor de um produto: '))

print('À vista, no dinheiro ou cheque, digite 1.\nÀ vista no cartão, digite 2.\n2 vezes no cartão, digite 3.\n3 vezes no cartão, digite 4.')

y = int(input('Forma de pagamento: '))

if y == 1:
    z = x - (x * 0.1)
    print('Com o desconto de 10%, você pagará {:.2f} reais.'.format(z))
elif y == 2:
    z = x - (x * 0.05)
    print('Com o desconto de 5%, você pagará {:.2f} reais'.format(z))
elif y == 3:
    z = x / 2
    print('Você não receberá descontos e pagará {:.2f} rais por mês.'.format(z))
elif y == 4:
    z = x + (x * 0.2)
    a = z / 3
    print('Você recebeu 20% de juros e pagará {:.2f} reais por mês'.format(z))
