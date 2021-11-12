import random

w = str(input('Alune 1:'))
x = str(input('Alune 2:'))
y = str(input('Alune 3:'))
z = str(input('Alune 4:'))

r = [w, x, y, z]
random.shuffle(r)

print('A ondem que será apresentada é {}')
print(r)