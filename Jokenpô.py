import random

print("######JOKENPÔ######")
print("---------------------------------- // ----------------------------------")
print("\033[1mRegras do Jokenpô!\033[0m\nVocê possui \033[4mtrês escolhas\033[0m: pedra, papel ou tesoura.\n")
print("\033[1mComo ganhar?:\033[0m Quem joga pedra vence de tesoura, tesoura vence de papel e papel vence de pedra.")
print("\033[1mOpções de jogo:\033[0m Player vs Player (PvP) = 1, Player vs Computador (PvC) = 2 e Computador vs Computador (CvC) = 3.")
print("---------------------------------- // ----------------------------------")
modo = input("Digite seu modo de jogo (1, 2 ou 3): \n")
# palavra = "CABEÇA"
# palavra.lower()
# print(palavra.lower())

# Sugestões
# j = resultado_um/resultado_dois; escolha_jogador1/escolha_jogador2; jogada_jogador1/jogada_jogador2; jogada_p1/jogada_p2; acao_jogador1/acao_jogador2
# p = pontuacao_player_um/pontuacao_player_dois;...

p1 = 0
p2 = 0

while modo != "1" and modo != "2" and modo != "3":

    # programa continua rodando mesmo se o usuário digitar o modo incorretamente. Sem o input modo, o programa vai repetir infinitamente
    # o input acima. Não é recomendado tirar

    print("Esse modo não existe! Tente novamente.")
    modo = input("Digite seu modo de jogo (1, 2 ou 3): \n")

while modo == "1":

# Sugestões: 
# Player Um, faça a sua jogada! (Pedra, Papel ou Tesoura); O que você escolherá? (Pedra, Papel ou Tesoura); Eu escolho você! (Pedra, Papel ou Tesoura);... 

    j1 = input("Digite j1: ")

    j2 = input("Digite j2: ")

# Probabilidades vitória  = {1º pedra x tesoura; 2º tesoura x papel; 3º papel x pedra}

    # if j1.lower() and j2.lower() != ("pedra" or "papel" or "tesoura"):

    if (j1.lower() != "pedra" and j1.lower() != "papel" and j1.lower() != "tesoura") or (j2.lower() != "pedra" and j2.lower() != "papel" and j2.lower() != "tesoura"):
        
        print("Por favor, selecione uma jogada válida.")
        # Continua o loop até que o usuário acerte as palavras necessárias. Poderia deixar sem o continue, mas então, aparecia o "CONTINUAR" ou "SAIR" toda vem
        # que digitasse algo errado.
        # continue irá ignorar o erro e vai voltar no loop

        continue

    elif j1.lower() == j2.lower():

        print("\033[1mEMPATE!!!\033[0m")
        print(str(p1) + " - "  + str(p2))
        # print(f"{p1} - {p2}")

    elif j1.lower() == 'pedra' and j2.lower() == "tesoura":

        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - "  + str(p2))

    elif j1.lower() == 'tesoura' and j2.lower() == 'papel':

        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2)) 

    elif j1.lower() == 'papel' and j2.lower() == 'pedra':

        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2))

# ----------------------------------   ----------------------------------   ----------------------------------   ----------------------------------   

    elif j2.lower() == 'pedra' and j1.lower() == 'tesoura':

        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1)+ " - " + str(p2))

    elif j2.lower() == 'tesoura' and j1.lower() == 'papel':

        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    elif j2.lower() == 'papel' and j1.lower() == 'pedra':

        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(p1) + " - " + str(p2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Bonfim, Edoarda Cenci, Grazielle Claus\n")
            # se usar o break, vai sair apenas do while da linha 91. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")

# ----------------------------------------------------------------------------------------------------------------------------------------   

while modo == "2":

# pedra = 1, papel = 2, tesoura = 3

    j1 = input("Digite j1: ")
    j2 = random.randint(1,3)

    if j1.lower() != "pedra" and j1.lower() != "papel" and j1.lower() != "tesoura":
        
        print("Por favor, selecione uma jogada válida.")
        continue

    if (j1.lower() == "pedra" and j2 == 1) or (j1.lower() == "papel" and j2 == 2) or (j1.lower() == "tesoura" and j2 == 3):

        print("\033[1mEMPATE!!!\033[0m")
        print(str(p1) + " - " + str(p2))

    elif j1.lower() == 'pedra' and j2 == 3:

        print("j2 escolheu tesoura\n")
        print("\033[1mj1 venceu a rodada!\033[0m")
        p1 += 1
        print(str(p1) + " - "  + str(p2))

    elif j1.lower() == 'tesoura' and j2 == 2:

        print("j2 escolheu papel\n")
        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2)) 

    elif j1.lower() == 'papel' and j2 == 1:

        print("j2 escolheu pedra\n")
        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2))

# ---------------------------------- // ---------------------------------- // ---------------------------------- // ----------------------------------   

    elif j2 == 1 and j1.lower() == 'tesoura':

        print("j2 escolheu pedra\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1)+ " - " + str(p2))

    elif j2 == 3 and j1.lower() == 'papel':

        print("j2 escolheu tesoura\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    elif j2 == 2 and j1.lower() == 'pedra':

        print("j2 escolheu papel\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(p1) + " - " + str(p2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Bonfim, Edoarda Cenci, Grazielle Claus\n")
            # se usar o break, vai sair apenas do while da linha 91. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")

# ----------------------------------------------------------------------------------------------------------------------------------------   

while modo == "3":

    j1 = random.randint(1,3)
    j2 = random.randint(1,3)

    if j1 == j2:

        print("\033[1mEMPATE!!!\033[0m")
        print(str(p1) + " - " + str(p2))

    elif j1 == 1 and j2 == 3:

        print("j1 escolheu pedra")
        print("j2 escolheu tesoura\n")
        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - "  + str(p2))

    elif j1 == 3 and j2 == 2:

        print("j1 escolheu tesoura")
        print("j2 escolheu papel\n")
        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2)) 

    elif j1 == 2 and j2 == 1:

        print("j1 escolheu papel")
        print("j2 escolheu pedra\n")
        print("\033[1mj1 venceu a rodada\033[0m")
        p1 += 1
        print(str(p1) + " - " + str(p2))

# ---------------------------------- // ---------------------------------- // ---------------------------------- // ----------------------------------   

    elif j2 == 1 and j1 == 3:

        print("j1 escolheu tesoura")
        print("j2 escolheu pedra\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1)+ " - " + str(p2))

    elif j2 == 3 and j1 == 2:

        print("j1 escolheu papel")
        print("j2 escolheu tesoura\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    elif j2 == 2 and j1 == 1:

        print("j1 escolheu pedra")
        print("j2 escolheu papel\n")
        print("\033[1mj2 venceu a rodada\033[0m")
        p2 += 1
        print(str(p1) + " - " + str(p2))

    while True:

        saida = input("Deseja CONTINUAR ou SAIR?\n")

        if saida.lower() == "continuar":

            break

        elif saida.lower() == "sair":

            print("\n")
            print("Placar Final: \n")
            print("Jogador 1 | Jogador 2")
            print("        " + str(p1) + " - " + str(p2))
            print("Adeus. Obrigada por testar o nosso programa!!\n")
            print("Participantes: Julia Bonfim, Edoarda Cenci, Grazielle Claus\n")
            # se usar o break, vai sair apenas do while da linha 91. Exit é usado para terminar o programa de vez
            exit()

        else:

            print("Algo deu errado. Tente digitar o comando novamente")

# Sugestões

# adicionar regras

# ------------------------------------------------------------------------------------

# O que falta?

# Comentários pelo código. 
# "6. O código do programa deve estar documentado"

# Cada um estudar sobre o programa."
# 7. Os estudantes devem ter domínio sobre todo o código, será realizado um teste de autoria nas entregas para avaliar o domínio de cada estudante."