# Daniel dos Santos e Lucas Rodrigues

#1.
def vitoria(tabuleiro,criterio):
    """Função que recebe um tabuleiro com em formato de matriz 4x4 e identifica se possui um multiplo de dois dado no criterio e retorna se possui ou não possui
matriz, int -> boolean"""
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 2**criterio:
                 return True
    return False
#2.
import random
def dois_ou_quatro(tabuleiro):
    """Função que ao receber um tabuleiro em formato de matriz 4x4 verifica quais posições que possuem 0 e retorna uma matriz com as posições zero preenchidas com 2 ou 4 aleatoriamente
matriz -> matriz"""
    matriz_zero =[]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == 0:
                list.append(matriz_zero,[i,j])
                
    if matriz_zero != 0:
        matriz_zero = random.sample(matriz_zero, 1)
        i_aleatorio, j_aleatorio = matriz_zero[0]
        tabuleiro[i_aleatorio][j_aleatorio] = random.choices([2,4],[60,40],k=1)[0]

# Daniel dos Santos e Lucas Rodrigues

# 1)

def mostra_tabuleiro(tabuleiro):
    '''Recebe o estado atual do tabuleiro numa matriz e o imprime.
    ASSUME QUE a matriz recebida só possui elementos com comprimentos no intervalo de 1 a 4.
    matriz --> None'''
    for linha in tabuleiro:
        # Formatação das casas para que todas tenham o mesmo tamanho
        linha_formatada = ''
        for casa in linha:
            if len(str(casa))== 4:
                linha_formatada += str.format(' {} ', casa)
            if len(str(casa)) == 3:
                linha_formatada += str.format(' {}  ', casa)
            if len(str(casa)) == 2:
                linha_formatada += str.format('  {}  ', casa)
            if len(str(casa)) == 1:
                linha_formatada += str.format('  {}   ', casa)
        # Impressão em formato de tabuleiro
        print(str.format('|{}|', linha_formatada))

# 2)        

def esquerda(tabuleiro):
    '''Faz o movimento para a esquerda no tabuleiro, recebido em formato de matriz.
    ASSUME QUE a matriz recebida tem dimensões 4 x 4
    matriz --> None'''
    j = 0
    for linha in tabuleiro:
        # Filtragem das casas preenchidas
        casas_preenchidas = []
        for casa in linha:
            if casa != 0:
                list.append(casas_preenchidas, casa)
        # Soma dos números vizinhos repetidos
        i = 1
        while i < len(casas_preenchidas):
            if casas_preenchidas[i-1] == casas_preenchidas[i]:
                casas_preenchidas[i-1] += casas_preenchidas[i]
                casas_preenchidas[i] = 0
                i = i + 1
            else:
                i = i + 1
        # Deslocamento dos números adjacentes à casas vazias 
        i = 1
        while i < len(casas_preenchidas):
            if casas_preenchidas[i-1] == 0:
                casas_preenchidas[i-1] = casas_preenchidas[i]
                casas_preenchidas[i] = 0
                i = i + 1
            else:
                i = i + 1
        # Atualizando o tabuleiro
        tabuleiro[j] = casas_preenchidas + [0]*(4 - len(casas_preenchidas))
        j = j + 1

def direita(tabuleiro):
    '''Faz o movimento para a direita no tabuleiro, recebido em formato de matriz.
    ASSUME QUE a matriz recebida tem dimensões 4 x 4
    matriz --> None'''
    j = 0
    for linha in tabuleiro:
        # Filtragem das casas preenchidas
        casas_preenchidas = []
        for casa in linha:
            if casa != 0:
                list. append(casas_preenchidas, casa)
        # Soma dos números vizinhos repetidos
        i = len(casas_preenchidas) - 1
        while i > 0:
            if casas_preenchidas[i-1] == casas_preenchidas[i]:
                casas_preenchidas[i] += casas_preenchidas[i-1]
                casas_preenchidas[i-1] = 0
                i = i - 1
            else:
                i = i - 1
        # Deslocamento dos números adjacentes à casas vazias
        i = len(casas_preenchidas) - 1
        while i > 0:
            if casas_preenchidas[i] == 0:
                casas_preenchidas[i] = casas_preenchidas[i-1]
                casas_preenchidas[i-1] = 0
                i = i - 1
            else:
                i = i - 1
        # Atualizando o tabuleiro
        tabuleiro[j] = [0]*(4 - len(casas_preenchidas)) + casas_preenchidas
        j = j + 1
            



