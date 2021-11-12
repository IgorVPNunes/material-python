from exe115 import *
from exe115.ManipArq import *

resposta = menu([ 'Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    if resposta == 1:
        lerArq(arq)
    elif resposta == 2:
        linhas()
        print('\033[31mNOVO CADASTRO\033[m'.center(45))
        linhas()
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        adicionar(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        linhas()
        print('Muito obrigado e volte sempre!')
        linhas()
        break
