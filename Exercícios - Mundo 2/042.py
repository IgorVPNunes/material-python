print('Digite o valor dos três lados de um triângulo.')
x = float(input('Primeira medida:'))
y = float(input('Segunda medida:'))
z = float(input('Terceira medida:'))

a = x + y
b = x + z
c = y + z

if a >= z and b >= y and c >= x:
    if x == y == z:
        print('Você poderá construir um triângulo equilátero.')
    elif x == y != z or x == z != y or y == z != x:
        print('Você poderá construir um triângulo isóceles.')
    elif x != y != z != x:
        print('você poderá construir um triangulo escaleno.')
else:
    print('Com essas medidas não é possível montar um triângulo.')
