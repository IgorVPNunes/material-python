x = float(input('Digite o comprimento (em metros) de uma parede:'))
y = float(input('Digite a largura (em metros) dessa mesma parede:'))

a = x * y
n = a / 2

print('Considerando que essa parede tem {} metros quadrados, será(ão) necessária(s) {} lata(s) de tinta para pintá-las'.format(a,n))
