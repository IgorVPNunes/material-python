a = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while a not in 'MF':
    a = input('Tente novamente:')
print('Muito obrigado!')
