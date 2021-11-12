a = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalho', 'mercado',
     'programador', 'futuro')
b = len(a)
d = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for c in a:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for e in c:
        if e.upper() in d:
            print(e, end=' ')
