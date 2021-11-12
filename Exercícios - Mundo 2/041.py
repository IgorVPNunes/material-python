from datetime import date

print('Considerando a tabela a seguir:\nMirim: até 9 anos\nInfantil: até 14 anos\nJunior: até 19 anos\nSênior: até 20 anos\nMaster: a partir de 25 anos')
print(' \n ')
x = int(input('Digite o seu ano de nascimento:'))
y = date.today().year
z = y - x

if z <= 9:
    print('Você está na categoria MIRIM')
elif 9 < z <= 14:
    print('Você está na categoria INFANTIL')
elif 14 < z <= 19:
    print('Você está na categoria JUNIOR')
elif 19 < z <= 25:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER')
