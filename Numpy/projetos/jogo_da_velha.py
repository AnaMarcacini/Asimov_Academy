import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    # Coloca uma peça (1 ou 2) no tabuleiro
    tabuleiro[linha][coluna] = peca

def verificar_vitoria(tabuleiro, peca):
    # Verifica se o jogador venceu
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)

    # Se não houver vencedor, retorna False
    return any([linhas, colunas, diagonais])

def jogar():
    # Executa o jogo
    tabuleiro = np.zeros((3, 3))
    peca_atual = 1
    vencedor = False
    empate = False

    # Loop principal do jogo
    while not vencedor and not empate:
        # Imprime o tabuleiro
        print(tabuleiro)

        # Pede ao jogador atual para escolher uma posição
        while True:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            if not any(x > 2 for x in [linha, coluna]):
                break
            print('\nEscolha linhas e colunas válidas! De 0 a 2\n')

        # Verifica se a posição escolhida é válida
        if tabuleiro[linha][coluna] != 0:
            print("\nPosição ocupada!\n")
            continue

        # Coloca a peça no tabuleiro e verifica se o jogador atual venceu
        colocar_peca(tabuleiro, linha, coluna, peca_atual)
        vencedor = verificar_vitoria(tabuleiro, peca_atual)

        # Verifica se houve empate
        if np.all(tabuleiro != 0):
            empate = True

        # Passa a vez para o próximo jogador
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    # Imprime o resultado do jogo
    print(tabuleiro)
    if vencedor:
        print("\n\n\tParabéns, jogador", peca_atual, "venceu! ====================")
    else:
        print("\n\n\tEmpate! ====================")


# Executa o jogo
jogar()
