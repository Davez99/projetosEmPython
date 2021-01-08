# projeto final 2.0.6

# Exercício projeto final parte 2 jogo "jokenpo"
# menu de escolha inicial
def menu_inicial():
    print("Pedra - 1")
    print("Papel - 2")
    print("Tesoura - 3")

    jogador = int(input("Vamos jogar? Faça sua escolha:"))
    if jogador >= 4:
        print("JOGADA INVALIDA! AS OPÇÕES SÃO 1,2 OU 3 AMIGÃO")
        return menu_inicial()
    # Jokepô executável
    from random import randint
    from time import sleep

    itens = ("Pedra", "Papel", "Tesoura")
    computador = randint(1, 3)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ!")
    print("%%" * 20)
    print("O computador escolheu {}".format(itens(computador)))
    print("Você escolheu {}".format(itens(jogador)))
    print("%%" * 20)
    # Parametro vencedor, empate, derrota
    if computador == 1 and jogador == 3:  # cpu vence do jogador
        p = str("perdeu")
        empates.append(p)
        print("COMPUTADOR VENCEU")
    elif computador == 2 and jogador == 1:
        p = str("perdeu")
        empates.append(p)
        print("COMPUTADOR VENCEU")
    elif computador == 3 and jogador == 2:
        p = str("perdeu")
        empates.append(p)
        print("COMPUTADOR VENCEU")
    if computador == 3 and jogador == 1:# cpu perde do jogador
        v = str("venceu")
        vitorias.append(v)
        print("JOGADOR VENCEU")
    elif computador == 2 and jogador == 3:
        v = str("venceu")
        vitorias.append(v)
        print("JOGADOR VENCEU")
    elif computador == 1 and jogador == 2:
        v = str("venceu")
        vitorias.append(v)
        print("JOGADOR VENCEU")
    if computador == 1 and jogador == 1:  # cpu empata com o jogador
        e = str("empatou")
        empates.append(e)
        print("EMPATE")
    elif computador == 2 and jogador == 2:
        e = str("empatou")
        empates.append(e)
        print("EMPATE")
    elif computador == 3 and jogador == 3:
        e = str("empatou")
        empates.append(e)
        print("EMPATE")
    return jogador

#pergunta para jogar de novo
def jogar_novamente():
    print("QUER JOGAR MAIS UMA?")

    jogador = str(input("S para sim e N para não:"))
    while jogador == "s":
        return menu_inicial() and jogar_novamente()
    if jogador == "n":

        exit()
    else:
        print("OPÇÃO INVALIDA MEU GAROTO, OU É 'S' OU É 'N'")
        return jogar_novamente()

def game_result (jogador):
    if jogador == "v":
        print("Você venceu {} vezes".format(game_vitorias (jogador)))
    elif jogador == "p":
        print("Você perdeu {} vezes".format(game_result (jogador)))
    elif jogador == "e":
        print("Você empatou {} vezes".format(game_result (jogador)))
    else:
        print("Esses foram os resultados")
        return game_result (jogador)

    return jogador
#armazenamento de jogadas
vitorias = []
empates = []
derrotas = []

menu_inicial()
jogar_novamente()
game_result ()



