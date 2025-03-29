import numpy as np

# Cria um mapa de 5 x 5 com números aleatórios de 1 a 9
mapa = np.random.randint(1, 10, size=(5, 5))

# Esconde o tesouro em uma célula aleatória do mapa, verificando que não seja a celula onde o jogador nasce
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

# Define a posição e pontuação inicial do jogador 
posicao_jogador = (0, 0)
pontuacao = 0

# Loop principal do jogo
while True:
    mapa_com_jogador = np.copy(mapa)
    mapa_com_jogador[posicao_jogador] = 0
    print(mapa_com_jogador)

    # Pede ao jogador para escolher uma direção para se mover
    direcao = input('Digite a direção que deseja se mover (cima, baixo, esquerda, direita): ')
    if direcao == 'cima' or direcao == 'c':
        nova_posicao = (posicao_jogador[0] - 1, posicao_jogador[1])
    elif direcao == 'baixo' or direcao == 'b':
        nova_posicao = (posicao_jogador[0] + 1, posicao_jogador[1])
    elif direcao == 'esquerda' or direcao == 'e':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1] - 1)
    elif direcao == 'direita' or direcao == 'd':
        nova_posicao = (posicao_jogador[0], posicao_jogador[1] + 1)

    # Verifica se a nova posição é válida (dentro do mapa)
    if nova_posicao[0] < 0 or nova_posicao[0] >= mapa.shape[0] or nova_posicao[1] < 0 or nova_posicao[1] >= mapa.shape[1]:
        print('Posição inválida!')
        continue

    # Atualiza a posição do jogador e a pontuação
    posicao_jogador = nova_posicao
    pontuacao += 1

    # Verifica se o jogador encontrou o tesouro
    if posicao_jogador == (tesouro_linha, tesouro_coluna): break

print('\n\n======= Parabéns, você encontrou o tesouro =========')
print(f'PONTUAÇÃO FINAL: {pontuacao}')
print(f'O tesouro estava em {tesouro_linha, tesouro_coluna}')
