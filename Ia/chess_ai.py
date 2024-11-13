# Função de avaliação do tabuleiro
def avaliar_tabuleiro(board):
    return sum(board.values())

# Função minimax com poda alfa-beta
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0:
        return avaliar_tabuleiro(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in gerar_movimentos(board, "branca"):
            resultado = executar_movimento(board, move)
            eval = minimax(resultado, depth - 1, alpha, beta, False)
            desfazer_movimento(board, move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in gerar_movimentos(board, "preta"):
            resultado = executar_movimento(board, move)
            eval = minimax(resultado, depth - 1, alpha, beta, True)
            desfazer_movimento(board, move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Função para escolher o melhor movimento
def escolher_melhor_movimento(board, depth=3):
    melhor_movimento = None
    melhor_valor = float('-inf')
    for move in gerar_movimentos(board, "branca"):
        resultado = executar_movimento(board, move)
        movimento_valor = minimax(resultado, depth - 1, float('-inf'), float('inf'), False)
        desfazer_movimento(board, move)
        if movimento_valor > melhor_valor:
            melhor_valor = movimento_valor
            melhor_movimento = move
    return melhor_movimento

# Funções simuladas para geração de movimentos e execução
def gerar_movimentos(board, cor):
    return [("peça", "origem", "destino")]

def executar_movimento(board, move):
    return board

def desfazer_movimento(board, move):
    pass