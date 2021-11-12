'''
print('') #escrever algo
x = input('') #receber informações
x1 = x #variável = objeto
x2 = x
------------------------------------------------------------------------------------------------------------------------
O símbolo '=' é recebe o objeto
O símbolo '==' é igual
O símbolo '!=' é diferente
------------------------------------------------------------------------------------------------------------------------
print('algum texto q precise de uma ou mais variáveis como {} e {}. Vai ficar na ordem.').format(x1, x2)
------------------------------------------------------------------------------------------------------------------------
OPERADORES ARITIMÉTICOS
    x + x #soma
    x - x #subtração
    x * x #multiplicação
    x / x #divisão
    x ** x #potenciação
    x // x #parte inteira da divisão
    x % x #resto da divisão
------------------------------------------------------------------------------------------------------------------------
TIPOS PRIMITIVOS
x1 = int() #número inteiro - (7/-4/0 etc)
x2 = float() #números reais - (4.5/0.005/-15.2/7.0 etc)
x3 = bool() #valores lógicos - (True / False)
x4 = str() #valores de caracteres - ('Olá'/'7,5'/'')
------------------------------------------------------------------------------------------------------------------------
type(x) #descobre tipo primitivo da variável
------------------------------------------------------------------------------------------------------------------------
x.issomething #Indica se a variável é alguma coisa
------------------------------------------------------------------------------------------------------------------------
BIBLIOTECAS
'import biblioteca'
'from biblioteca import comando'
    MATH
    ceil - arredonda para cima
    floor - arredonda para baixo
    trunc - exclui os números depois da vírgula
    pow - potênciação (substitui o **)
    sqrt - raiz quadrada
    factorial - fatorial

    NOVAS BIBLIOTECAS
    settings
    Project:PythonCourse
    python interpreter
    +
------------------------------------------------------------------------------------------------------------------------
RANDOM
os objetos ficam entre colchetes []
random.choice() - escolhe um único elemento
random.shuffle() - torna a ordem dos elementos aleatória
------------------------------------------------------------------------------------------------------------------------
PYGAME
Iniciar pygame
    pygame.init()
tocarmusica
    pygame.mixer.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy()): pass
------------------------------------------------------------------------------------------------------------------------
TIME
sleep(segundos) - coloca o processamento para esperar os segundos desejados
------------------------------------------------------------------------------------------------------------------------
DATETIME
date.today().year - identifica o ano do computador
------------------------------------------------------------------------------------------------------------------------
NÚMERO DE CASAS DECIMAIS
Dentro do {} colocar :.xf, sendo x o número de casas desejadas.
{:. f}
------------------------------------------------------------------------------------------------------------------------
DIVIDIR A FRASE PARA OUTRA LINHA
'\n'
------------------------------------------------------------------------------------------------------------------------
CADEIA DE TEXTO (STRING)
    string = frase
    toda string deve estar entre aspas(simples ou duplas)
MANIPULAÇÃO DE STRING
    quando um string é inserido no python, ele divide cada caractere em índices, que começam no 0 e terminam onde a frase terminar
FATIAMENTO
    x[9] - Caractere 10 da frase x (Fatiamento de um único elemeno)
    x[9:13] - Caracteres do 10 elemento até o 13 elemento {exclui a última string} (fatiamento de múltiplos elementos)
    x[9:13:2] - Caracteres do 10 elemento até o 13 elemento, mas de dois em dois (fatiamento de múltiplos elementos)
    x[:5] - Do início ao elemento 4 ([:5] = [0:5]) {exclui a última string}
    x[15:] - Do elemento 15 ao final ([15:] = [15:'n final']) {exclui a última string}
    x[9::3] - Do elemento 10 ao fina, mas de 3 em 3.
ANÁLISE
    len(x) - comprimento da frase (quantos elementos/caracteres)
    x.count(caractere) - conta quantas vezes o caractere aparece na frase {pode se colocar uma divisão de string para reduzir o espaço de procura Ex.:x.count(a,0,9)}
    x.find(caracteres) - encontra onde o caractere (ou uma sequencia) começa dentro da frase {se for colocado uma sequencia de caracteres que não está presente na frase, será retornado o número -1}
    'palavra' in x - verifica a presença da sequência de caracteres na frase (true ou false)
TRANSFORMAÇÃO
    x.repplace('palavra 1', 'palavra 2') - troca a sequência de caractere por outra
    x.upper() - transforma todas as letras da frase em maiúsculas
    x.lower() - transforma todas as letras da frase em minúsculas
    x.capitalize() - transforma todas as letras da frase em minúsculas e só a primeira letra da frase em maiúsculas
    x.title() - transforma todas as letras da frase em minúsculas e só as primeiras letras das palavras em maiúsculas
    x.strip() - remove os espaços inúteis no início e no final {pode ser utiizado as letras r(direita) ou l(esquerda) para especificar o lado que se deseja excluir os espaços}
DIVISÃO
    x.split() - divide a frase onde houver espaços
JUNÇÃO
    'caracter desejado entre as palavras'.join(x) - junta as palavras com o caracter escohido entre elas
------------------------------------------------------------------------------------------------------------------------
CONDIÇÕES
Indentação - comandos que só são feitos sob uma condição (estão mais a direita)
if (se) x.alguma_coisa():
    bloco True
else (senão):
    bloco False
print('Alguma coisa')
Condição Simplificada
print('Aguma coisa'if x alguma coisa else outra coisa)

Sem else - condicional simples
Com else - condicional composta

ANSI - Padrão de normalização nacional
    escape sequence - \'código'
------------------------------------------------------------------------------------------------------------------------
CORES
print('\033[style:text:backmTEXTO')
#não é obrigatório colocar todos e não precisa seguir essa ordem
#se quiser tirar da linha toda é só colocar um  \033[m no final
    Tipos de código
        style - estilo da fonte
            0 - normal
            1 - negrito
            4 - sublinhado
            7 - inveerter as configurações de cor (troca a cor da letra com a do fundo)
        text - cor do texto
            30 - branco
            31 - vermelho
            32 - verde
            33 - amarelo
            34 - azul
            35 - roxo
            36 - ciano
            37 - cinza
        back - cor do fundo
            40 - branco
            41 - vermelho
            42 - verde
            43 - amarelo
            44 - azul
            45 - roxo
            46 - ciano
            47 - cinza
'''