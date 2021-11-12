#forma do guanabara
from math import factorial
a = int(input('Digite um número inteiro:'))
b = factorial(a)
print(f'O fatorial de {a} é {b}.')

'''
#minha forma
print('')
a = int(input('Digite um número inteiro:'))
b = a
c = 0
while a != 1:
    a = a-1
    b *= a
print(f'O fatorial desse número é {b}.')
'''
