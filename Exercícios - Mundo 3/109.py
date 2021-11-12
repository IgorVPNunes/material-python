from utilidadesCeV import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p, x=True)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p, x=True)}')
print(f'Aumentando 10% de {Moeda.moeda(p)}, temos {Moeda.aumentar(p, 10, x=True)}')
print(f'Diminuido 13% de {Moeda.moeda(p)}, temos {Moeda.diminuir(p, 13, x=True)}')
