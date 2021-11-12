k = float(input('Digite quantos quilômetros você andou com o carro alugado:'))
d = int(input('Digite quantos dias você ficou com o carro alugado:'))

pd = 60 * d
pk = 0.15 * k
p = pd + pk

print('Considerando que o preço por dia é de R$60.00 e por Km é de R$0,15, você deverá pagar `R${}'.format(p))
