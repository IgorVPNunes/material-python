'''
VARIAVEIS COMPOSTAS

    TUPLAS
    -Um tipo de variável com vários espaços
    -Valores definidos de espaços
    -Os elementos sao identificados por índices ([0], [1], [2], [3] etc)
    -SÃO IMUTÁVEIS
    -Recebem todos os tipos de elemento (int, float, str etc) e nao os alteram.
    -Representação:
        tupla = (elementos) ou x = elementos

    OBS'1: enumerate(variável) -> localiza as posições dos elementos numa tupla.
    OBS'2: sorted(variável) -> coloca os elementos da tupla em ordem alfabética.
    OBS'3: tupla1 + tupla2 = tupla1tupla2 (cria outra tupla com todos os elementos) (a união com b) (a ordem faz diferença).
    OBS'4: tupla.index(elemento) -> indica a posição do elemento dentro da tupla (somente o primeiro elemento, ou apartir de  se colocado index(eemento, x)).
    OBS'5: del(variável) -> apaga a variavel toda.
    OBS'6: tuple(x) -> transforma x em uma tupla


    LISTAS
    -Praticamente iguais as tuplas
    -SÃO MUTÁVEIS
    -Representação:
        lista = [elementos]

    OBS'1: lista.append(elemento) -> adiciona um elemento à lista na útima posição
    OBS'2: lista.insert(x, elemento) -> adiciona um elemento à lista na posição x
    OBS'3: list(x) -> transforma x em uma lista
    OBS'4: del lista[x] -> apaga o elemento x(posição) da lista
    OBS'5: lista.pop(x) -> apaga o elemento x(posição) da lista
        Se usado sem elementos entre os parenteses, ele elimina o último elemento
    OBS'6: lista.remove(x) -> apaga o elemento x(o elemento) da lista
    OBS'7: lista.sort() -> coloca os elementos da lista em ordem numérica crescente
    OBS'8: lista.sort(reverse=True) -> coloca os elementos da lista em ordem numérica decrescente]
    OBS'9: lista1 = lista2 -> o que altera em uma, altera na outra(ligação)
    OBS'10:lista1 = lista2[:] -> uma é cópia da outra
    OBS'11:lista1.append(lista2[:])


    DICIONÁRIOS
    -Representação:
        dicio = {'identificador'(chave):elemento(valores)}

    OBS'1: dicio['identificador'(chave):elemento(valores)] -> cria um novo idetificador
    OBS'2: dicio.values() -> identfica os valores (elementos)
    OBS'3: dicio.keys() -> identifica as chaves (identificadores)
    OBS'4: dicio.items() -> identifica os itens (valores + chaves)
    OBS'5: dicio.copy() -> cria uma copia do dicionario (semelhante ao lista[:])
------------------------------------------------------------------------------------------------------------------------
MAIORES E MENORES VALORES

    MAIOR
        max(variavel composta)
    MENOR
        min(variáve composta)
------------------------------------------------------------------------------------------------------------------------
ITEMGETTER
    - Seleciona a chave de execução
    - from operato import itemgetter
    - key=itemgetter(posição)
------------------------------------------------------------------------------------------------------------------------
FUNÇÕES

    - Funções se aliam a rotinas
    - Cria comandos
    - def
    - entre o def e o comando precisa de 2 inhas de espaço

    def comando():
        o que vc quer q o comando faça
    comando()
    Ex.:
        def mostralinha():
            print('linha'*30)
        mostralinha()
        print('Sistema de alunos')
        mostralinha()
        mostralinha()
        print('Cadastro e funcionários')
        mostralinha()

    def comando2(x):
        o que vc quer q o comando faça
        o que vc quer q o comando faça x
        o que vc quer q o comando faça
    comando2('Algo que vai entrar no lugar de x')

    EMPACOTAMENTO DE FUNÇÕES
        def comando3(* y):
            o que vc quer q o comando faça
        comando3(numero x de elementos)
        - cria tuplas com os elementos

    FUNÇÕES COM LISTAS
        def comando4(z):
            o que vc quer q o comando faça
        comando4(lista)


    INTERACTIVE HELP
    Python Console
        help()
            Comando
    Manual de ajuda interativa do python
        -Qualquer comando digitado aparece uma lista de ajuda

    print(comando.__doc__)
        Manual de ajuda interativa do python
        -Qualquer comando digitado aparece uma lista de ajuda

    DOCSTRINGS
        Começa na inha depois do comando def
        """
        Manual completo que voce mesmo escreve
        """

    ARGUMENTOS OPCIONAIS
        def comando(x, y, z=a)
            x recebe um valor
            y recebe um valor
            se houver, z recebe um valor
            se não z recebe a

        qualquer variavel dentro do comando podem receber

    ESCOPO DE VARIÁVEIS
        Escopo global
            Declarada fora de def
                Serve para def e outros
        Escopo Local
            Declarada dentro de um def
                Serve apenas para o def
        OBS'1: Pode ocorrer de existirem duas variáveis iguais, se uma for local e a outro global
        OBS'2: Ao digitar, uma linha após o def, global variável
            Não e é criada outra variável e o a globa recebe o valor dado ao local

    RETORNO DE RESULTADOS
        return variável
        retorna o comando da variável interna do def para a variávell anterior ao comando

        Ex.: def comando(a, b)
                s = a + b
                return s

            resp = comando(2, 3) ou print(comando(2, 3))
            resp2 = comando(4, 5)
            print(f'A soma de 2 e 3 é {resp} e a de 4 e 5 é {resp2}.')

------------------------------------------------------------------------------------------------------------------------
MODULARIZAÇÃO

    MÓDULO
        - Separa os códigos principais dos códigos de funções.
        - Criar novo arquivo .py
            - Um para os códigos
            - Um para as funções
        - No arquivo dos códigos, importar o arquivo das funçoes
            - Ex.: import uteis
        - Antes do comando desejado, colocara o nome do arquivo das funções
            - Ex.: uteis.fatorial(x)

    PACOTES
        - Pasta de módulos separados por categorias
            - Ex.: números, strings, cores, etc
        - Sua importação funciona da mesma forma.
            - Ex.:  import uteis
                    ou
                    from uteis import cores
        - É identificado, no python, como uma pasta
            - No pycharm == python package
            - Em outros == ?
            - Ex.:  Pasta uteis
                        modulo cores
                        modulo datas
                        etc
        - É necessária a criação de um arquivo __init__.py em cada pasta

------------------------------------------------------------------------------------------------------------------------

TRATAMENTO DE ERROS

    try:
        comandos
    except: (podem haver vários)
        o que se deve fazer se o comando der erro
    else: (opcional)
        o que se deve fazer se o comando der certo
    finally: (opcional)
        o que se deve fazer, dando certo ou não

    OBS'1: except Exception as x:
                x.__comando classificador de x__
            identifica e mostra o erro
    OBS'2: except ValueError(ou outro):
                comando se ocorrer o erro expecífico
------------------------------------------------------------------------------------------------------------------------

VERIFICAÇÃO DE SITES POR PYTHON

import urllib.request

try:
    urllib.request.urlopen("url").getcode()
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('O site Pudim está acessível.')

'''