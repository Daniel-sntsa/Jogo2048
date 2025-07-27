# Daniel dos Santos e Lucas Rodrigues

import _2048_funcoes_Daniel_Lucas_Rodrigues 

 # 1)
 
def cima(tabuleiro):
    '''Faz o movimento para cima no tabuleiro, recebido em formato de matriz.
    ASSUME QUE a matriz recebida tem dimensões 4 x 4
    matriz --> None'''
    
    # Transposição da matriz trabuleiro
    tabuleiroT = [*zip(*tabuleiro)]
    for i in range(4):
        tabuleiro[i] = list(tabuleiroT[i])

    # Movimentação dos números
    _2048_funcoes_Daniel_Lucas_Rodrigues.esquerda(tabuleiro)
    
    # Transposição para voltar a disposição inicial
    tabuleiroT = [*zip(*tabuleiro)]
    for i in range(4):
        tabuleiro[i] = list(tabuleiroT[i])
    
def baixo(tabuleiro):
    '''Faz o movimento para baixo no tabuleiro, recebido em formato de matriz.
    ASSUME QUE a matriz recebida tem dimensões 4 x 4
    matriz --> None'''
    
   # Transposição da matriz trabuleiro
    tabuleiroT = [*zip(*tabuleiro)]
    for i in range(4):
        tabuleiro[i] = list(tabuleiroT[i])

    # Movimentação dos números
    _2048_funcoes_Daniel_Lucas_Rodrigues.direita(tabuleiro)
    
    # Transposição para voltar a disposição inicial
    tabuleiroT = [*zip(*tabuleiro)]
    for i in range(4):
        tabuleiro[i] = list(tabuleiroT[i])

# 2)

def tabuleiro_vazio():
    '''Cria e retorna uma matriz nula de dimensões 4 x 4.
    None --> matriz'''
    tabuleiro = []
    for i in range(4):
        list.append(tabuleiro, [0]*4)
    return tabuleiro

def derrota(tabuleiro):
    '''Recebe o estado atual do tabuleiro numa matriz e retorna True se jogador perdeu e False caso contrário.
    matriz --> boolean'''
    
    # Criação de cópias do tabuleiro para não alterá-lo
    tabuleiro_teste1 = tabuleiro[:]
    tabuleiro_teste2 = tabuleiro[:]
    tabuleiro_teste3 = tabuleiro[:]
    tabuleiro_teste4 = tabuleiro[:]

    # Comparação do tabuleiro com as cópias depois dos movimentos
    _2048_funcoes_Daniel_Lucas_Rodrigues.esquerda(tabuleiro_teste1)
    a = int(tabuleiro == tabuleiro_teste1)
    _2048_funcoes_Daniel_Lucas_Rodrigues.direita(tabuleiro_teste2)
    d = int(tabuleiro == tabuleiro_teste2)
    cima(tabuleiro_teste3)
    w = int(tabuleiro == tabuleiro_teste3)
    baixo(tabuleiro_teste4)
    s = int(tabuleiro == tabuleiro_teste4)

    # Resultado final
    if a + d + w + s == 4:
        return True
    else:
        return False
    
def main():
    '''Programa principal do jogo 2048'''

    print('------ Jogo 2048 ------\n')
    # Nível de dificuladade, com restrição de entrada
    criterio = int(input('Digite o nível de dificuladade (digite uma potência de 2 no intervalo de 2 a 2048):\n'))
    while criterio not in [2,4,8,16,32,64,128,256,512,1024,2048]:
        criterio = int(input('Digite o nível de dificuladade (digite uma potência de 2 no intervalo de 2 a 2048):\n'))

    # Geração do tabuleiro
    tabuleiro = tabuleiro_vazio()

    # Preenchendo os valores iniciais
    _2048_funcoes_Daniel_Lucas_Rodrigues.dois_ou_quatro(tabuleiro)
    _2048_funcoes_Daniel_Lucas_Rodrigues.dois_ou_quatro(tabuleiro)

    # Início do jogo
    _2048_funcoes_Daniel_Lucas_Rodrigues.mostra_tabuleiro(tabuleiro)
    vitoria = _2048_funcoes_Daniel_Lucas_Rodrigues.vitoria(tabuleiro, criterio)
    i = 0
    while vitoria == False:

        # Descrição dos movimentos e entrada do usuário
        i = i + 1
        print(str.format('\n - Jogada {} - \n', i))
        print('Digite w para mover para cima')
        print('Digite a para mover para a esquerda')
        print('Digite s para mover para baixo')
        print('Digite d para mover para a direita')
        print('Digite q para desistir\n')
        movimento = input('Digite seu movimento:')

        # Movimentação do tabuleiro
        if movimento == 'w':
            cima(tabuleiro)
        elif movimento == 'a':
            _2048_funcoes_Daniel_Lucas_Rodrigues.esquerda(tabuleiro)
        elif movimento == 's':
            baixo(tabuleiro)
        elif movimento == 'd':
            _2048_funcoes_Daniel_Lucas_Rodrigues.direita(tabuleiro)
        elif movimento == 'q':
            return print('\n --- Se esforce mais na próxima ---')
        print('\n--------------------------------------\n')
        _2048_funcoes_Daniel_Lucas_Rodrigues.dois_ou_quatro(tabuleiro)
        vitoria = _2048_funcoes_Daniel_Lucas_Rodrigues.vitoria(tabuleiro, criterio)
        _2048_funcoes_Daniel_Lucas_Rodrigues.mostra_tabuleiro(tabuleiro)

        # Mensagem de derrota
        if derrota(tabuleiro):
            return print('\n --- Você perdeu, mais sorte da próxima vez ---\n')

    # Mensagem de vitória
    print('\n --- PARABÉNS, VOCÊ VENCEU!!! ---')
            
if __name__ == '__main__':
    main()         
    


    
    
    
        
