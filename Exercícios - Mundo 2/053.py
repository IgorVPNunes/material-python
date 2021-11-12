x = str(input('Digite uma frase:'))
y = x.lower()
z = y.split()
i = ''.join(z)
b = ''
c = len(i)
for a in range(c - 1, -1, -1):
    b += i[a]
if b == i:
    print('Essa palavra é um palíndromo.')

'''a = len(i)
b = i[a - 1::-1]
c = i[0:]
print('{} {}'.format(b, c,))
if b == c:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase é normal.')'''
