from utilidadesCeV import Moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10% de {Moeda.moeda(p)}, temos {Moeda.moeda(Moeda.aumentar(p, 10))}')
print(f'Diminuido 13% de {Moeda.moeda(p)}, temos {Moeda.moeda(Moeda.diminuir(p, 13))}')
