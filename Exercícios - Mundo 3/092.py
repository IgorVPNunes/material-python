from datetime import date
dc = {}
apos = pre = 0
ano = date.today().year
dc['nome'] = str(input('Nome: '))
dc['nascimento'] = int(input('Ano de nascimento: '))
dc['ctps'] = int(input('Carteira de trabalho (0 - não tem): '))
if dc['ctps'] != 0:
    dc['contratacao'] = int(input('Ano de contratação: '))
    dc['salario'] = float(input('Salário: R$'))
    apos = ano - dc['contratacao']
    pre = ano - apos
idade = ano - dc['nascimento']
print('='*30)
print(f'Seu nome é {dc["nome"]}.')
print(f'Sua idade é {idade}.')
if dc['ctps'] == 0:
    print('Você não tem CTPS.')
elif dc['ctps'] != 0:
    print(f'Seu CTPS é {dc["ctps"]}.')
    print(f'Sua primeira contratação foi em {dc["contratacao"]}.')
    print(f'Seu salário tem o valor de R${dc["salario"]}.')
    if apos <= 35:
        print(f'Você poderá se aposentar daqui {apos} anos.')
    else:
        print(f'Você poderia ter se aposentado em {pre}.')
