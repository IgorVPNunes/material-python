'''
CONDIÇÕES ANINHADAS
if - se (obrigatório) - pode aparecer quantas vezes for necessário
elif - senão + se (opcional) - pode aparecer quantas vezes for necessário
else - senão (opcional) - só pode aparecer uma vez
------------------------------------------------------------------------------------------------------------------------
CONVERSORES AUTOMÁTICOS DE BASES
bin(x) - binário - 0b
oct(x) - octal - 0o
hex(x) - hexadecimal - 0x
------------------------------------------------------------------------------------------------------------------------
SUBSTITUIR O ENTER ENTRE AS LINHAS
, end= 'o que se deseja'
Se quiser excluir o enter, basta colocar , end= ''
------------------------------------------------------------------------------------------------------------------------
LOCALIZAÇÃO DE UM PRINT

    CENTRALIZAR
    print('texto'.center(intervalo de espaço))

    JOGAR PARA ESQUERDA
    print('texto'.ljust(intervalo de espaço))

    JOGAR PARA DIREITA
    print('texto'.rjust(intervalo de espaço))
------------------------------------------------------------------------------------------------------------------------
ESTRUTURAS DE REPETIÇÃO (OU ITERAÇÃO):

    ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE
    for x in range(0, y):
        if alguma coisa:
            comando_0
        comando_1
    comando_2

    OBS: intervalo pode ser 'até casa número y' ou 'y vezes'
    OBS_2: Se deseja numerar de forma diferente (para trás, de 2 em 2 etc), basta colocar intervalo , o qe deseja 1 (6, 0, -1 ou 2 etc)

    ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO
    while alguma coisa:
        if coisa_1:
            comando_0
        if coisa_2:
            comando_1
        if coisa_3:
            comando_2
    comando_3

    OBS: Precisa de igualar o elemento ao numero que se deseja iniciar e depois utiizar o elemento += 1 para aparecer todos.

    INTERRUPÇÃO DE WHILE
    while alguma coisa:
        if coisa_1:
            comando_0
        if coisa_2:
            comando_1
        if coisa_3:
            comando_2
            break
    comando_3

    OBS'2: Se usar 'while TRUE:' o while dura para sempre (ou até se tornar FALSE)
    OBS'3: continue é usado para retornar ao while
------------------------------------------------------------------------------------------------------------------------
SOMAR TODOS OS ELEMENTOS DE UMA LISTA
x = 0
x = x + lista ou x += lista
------------------------------------------------------------------------------------------------------------------------
CONTAR TODOS OS ELEMENTOS DE UMA LISTA
x = 0
x = x + 1 ou x += 1
------------------------------------------------------------------------------------------------------------------------
CRIANDO LISTAS COM NÚMEROS
x = list(range(último número da lista))
------------------------------------------------------------------------------------------------------------------------
ENCONTRAR TODOS OS ELEMENTOS DENTRO DE UMA LISTA
x = 'frase'
y = [i for i in range(len(x)) if a.startswith('elemento', i)]
print(y) - qual(is) posição(ões) o(s) 'elemento(s)' aparece(m)
'''