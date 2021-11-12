from utilidadesCeV import Moeda
from utilidadesCeV import dados

p = dados.leiaDinheiro('Digite o preço: R$')
Moeda.resumo(p, 35, 22)
