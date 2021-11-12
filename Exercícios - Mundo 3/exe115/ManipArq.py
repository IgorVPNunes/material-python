def linhas():
    print('-'*40)


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        linhas()
        print('\033[31mPESSOAS CADASTRADAS\033[m'.center(45))
        linhas()
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]}{" " * (38 - len(dado[1]))}{dado[1]}')
    finally:
        a.close()


def adicionar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Erro ao cadastrar a pessoa.')
        else:
            print(f'{nome.title()} adicionado com sucesso!')
            a.close()


