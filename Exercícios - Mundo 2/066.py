a = b = c =0
while True:
    a = int(input('Digite um número inteiro: '))
    if a == 999:
        break
    b += a
    c += 1
print('')
print(f'Você digitou {c} números e a soma entre eles é {b}!')
