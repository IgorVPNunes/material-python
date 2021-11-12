print('Digite 999 para parar!')
a = 0
b = int(input('Digite um número inteiro:'))
c = 0
while b != 999:
    if b != 999:
        a += 1
        c += b
        b = int(input('Digite um número inteiro:'))
print(f'Você digitou {a} números e a soma deles foi {c}!')
