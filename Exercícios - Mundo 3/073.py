a = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Flamengo', 'Atlético-PR', 'Ceará SC', 'Santos',
     'Atlético GO', 'Bahia', 'Corinthians', 'Fuminense', 'Juventude', 'Internacinal', 'Sport Recife', 'Cuiabá',
     'São Paulo', 'América MG', 'Grêmio', 'Chapecoense')
b = a[0:5]
c = a[-4:]
d = sorted(a)
e = a.index('Chapecoense')

print(f'Os cinco primeiros colocados são:\n{b}\n')
print(f'Os quatro últimos colocados são:\n{c}\n')
print(f'Os times em ordem alfabética ficam:\n{d}\n')
print(f'A Chapecoense está na posição {e + 1}.')
