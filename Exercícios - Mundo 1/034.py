x = float(input('Digite o valor do seu salário:'))

if x > 1250:
    a = (x * 0.1) + x
    print('Com o aumento de 10%, o seu sallário será de R${:.2f}.'.format(a))
else:
    b = (x * 0.15) + x
    print('Com o aumento de 15%, seu salário será de R${:.2f}.'.format(b))
