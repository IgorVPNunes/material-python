from utilidadesCeV import Moeda
from utilidadesCeV import dados

p = dados.leiaDinheiro('Digite um preço: R$')
Moeda.resumo(p, 35, 22)
