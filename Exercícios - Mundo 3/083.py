a = []
b = []
c = str(input('Digite uma expressão matemática: '))
d = len(c)
for e in c:
    if e == '(':
        a.append('(')
    if e == ')':
        b.append(')')
f = len(a)
g = len(b)
if f == g:
    print('Sua expressão está válida!')
if f != g:
    print('Sua expressão está inválida!')
