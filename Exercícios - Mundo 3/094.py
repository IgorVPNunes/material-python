td = []
pes = {}
ida = 0
f = []
me = []
while True:
    print('='*30)
    nome = str(input('Nome: ')).title()
    sexo = str(input('Sexo [m/f]: ')).lower()
    if sexo not in 'mf':
        print('Não identificado. Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [m/f]: ')).lower()
    if sexo == 'f':
        f.append(nome)
    idade = int(input('Idade: '))
    pes['nome'] = nome
    pes['sexo'] = sexo
    pes['idade'] = idade
    td.append(pes.copy())
    ida += idade
    tot = len(td)
    media = ida / tot
    if idade > media:
        me.append(nome)
    pes.clear()
    stop = str(input('Deseja continuar? [s/n]: ')).lower().strip()
    if stop not in 'sn':
        print('Não identificado. Por favor, digite apenas S ou N.')
        stop = str(input('Deseja continuar? [s/n]: ')).lower().strip()
    if stop in 'Nn':
        break
print('='*30)
print(f'O número de pessoas cadastradas foi {tot}.')
print(f'A média das idades é {media}.')
print(f'As mulheres cadastradas foram: {f}.')
print(f'As pessoas com idade acima da média são: {me}.')
