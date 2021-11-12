a = []
d = 0
while True:
    b = int(input('Digite um número inteiro: '))
    a.append(b)
    c = str(input('Deseja continuar? [s/n]: ')).lower()
    if c == 'n':
        break
print('-'*10)
print(f'Foram digitados {len(a)} valores.')
a.sort(reverse=True)
print(f'Os vallores digitados, em ordem decrescente, são: {a}')
if 5 in a:
    d = 'foi'
if 5 not in a:
    d = 'não foi'
print(f'O valor "5" {d} digitado.')
