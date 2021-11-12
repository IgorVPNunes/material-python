x = input('Digite o nome de uma cidade:')

a = x.strip()
b = a.title()
y = b.split()
z = 'Santo' in y

print('Essa cidade começa com "Santo"?:{}'.format(z))
