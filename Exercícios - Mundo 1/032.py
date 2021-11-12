import datetime

print('OBS: Se deseja analizar o ano atual, digite 0.')
x = int(input('Digite qual ano deseja analizar:'))


if x == 0:
    x = datetime.date.today().year

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('Esse é um ano bissexto.')
else:
    print('Esse ano não é bissexto.')
