x = int(input('Digite a velocidade de um carro:'))

if x > 60:
    a = (x - 60) * 7
    print('ALERTA! Você foi multuado em {} reais por estar acima de 60km/h.'.format(a))
else:
    print('Ok.')
