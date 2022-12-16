import random
import os
ListaMovimentos = ["papel", "pedra", "tesoura"]
PlacarJogador = 0
PlacarPC = 0
print("===============")
print("Bem vindo ao jogo Papel, Pedra e Tesoura")

def main_print ():
    print("======")
    print("\nPLACAR:")
    print("Você: {}". format (PlacarJogador))
    print("Computador: {}".format(PlacarPC))
    print("\n")
    print("Escolha seu lance:")
    print("0 Papel | 1 Pedra | 2 Tesoura")

def select_move():
    return random.choice(ListaMovimentos)


def get_jogada():
    while True:
        try:
            jogada = int(input())
            if jogada not in [0, 1, 2]:
                raise
            return ListaMovimentos [jogada]
        except Exception as e:
            print (e)

def select_winner (p_move, c_move):
    global PlacarJogador, PlacarPC

    if p_move == "pedra":
        if c_move == "tesoura":
            PlacarJogador += 1
            return "p"
        elif c_move == "papel":
            PlacarPC += 1
            return "c"
        else:
            return "e"
    if p_move == "papel":
        if c_move == "pedra":
            PlacarJogador += 1
            return "p"
        elif c_move == "tesoura":
            PlacarPC += 1
            return "c"
        else:
            return "e"


    if p_move == "tesoura":
        if c_move == "papel":
            PlacarJogador = 1
            return "p"
        elif c_move == "pedra":
            PlacarPC += 1
            return "c"
        else:
            return "e"



op = 1
while op == 1:
    main_print()
    jogada = get_jogada()
    JogadaPC = select_move()
    vitoria = select_winner (jogada, JogadaPC)
    print("")
    print("=================")
    print("Sua jogada: {}".format(jogada.upper()))
    print("Jogada do computador: {}".format(JogadaPC.upper()))
    if vitoria == "p":
        print("Você venceu!")
    elif vitoria == "c":
        print("Você perdeu!")
    else:
        print("Empate!")
    print("=================")
    while True:
        print("Jogar novamente? 0 - SIM | 1 - NÃO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            op = 0
        break
    os.system("clear")