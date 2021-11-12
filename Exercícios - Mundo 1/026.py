x = input('Digite uma frase:')
a = x.lower()
b = a.strip()
c = b.count('a')
d = b.find('a')
e = b.rfind('a')

print('Nessa frase aparecem {} vezes a letra "A"\nA primeira vez que ela aparece é na casa {}\nA útima vez que ela aparece é na casa {}'.format(c, d, e))
