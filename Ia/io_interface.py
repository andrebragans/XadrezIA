import json
import time

from Ia.chess_ai import escolher_melhor_movimento


# Função para salvar o estado do tabuleiro
def salvar_estado_tabuleiro(board, caminho_arquivo="data/tabuleiro.json"):
    with open(caminho_arquivo, 'w') as file:
        json.dump(board, file)

# Função para carregar o estado do tabuleiro
def carregar_estado_tabuleiro(caminho_arquivo="data/tabuleiro.json"):
    with open(caminho_arquivo, 'r') as file:
        board = json.load(file)
    return board

# Função para salvar o movimento da IA
def salvar_movimento(movimento, caminho_arquivo="data/movimento.json"):
    with open(caminho_arquivo, 'w') as file:
        json.dump(movimento, file)

# Loop para executar a IA e atualizar o movimento
def jogar_xadrez_ia():
    while True:
        time.sleep(1)  # Verifica atualizações a cada segundo
        try:
            # Carrega o estado do tabuleiro fornecido pelo Java
            board = carregar_estado_tabuleiro()
            # Calcula o melhor movimento
            movimento_ia = escolher_melhor_movimento(board)
            # Salva o movimento para que o Java leia e atualize o jogo
            salvar_movimento({
                "peca": movimento_ia[0],
                "origem": movimento_ia[1],
                "destino": movimento_ia[2]
            })
        except FileNotFoundError:
            continue