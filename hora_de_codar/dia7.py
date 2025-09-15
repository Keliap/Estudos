import random

def jogar_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")

    print("\nEscolha seu nível de dificuldade:")
    print("1. Fácil (10 tentativas)")
    print("2. Médio (7 tentativas)")
    print("3. Difícil (5 tentativas)")

    while True:
        dificuldade = input("Digite o número da dificuldade desejada: ")
        if dificuldade == "1":
            tentativas_totais = 10
            break
        elif dificuldade == "2":
            tentativas_totais = 7
            break
        elif dificuldade == "3":
            tentativas_totais = 5
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpites_feitos = []

    print("\nPensei em um número entre 1 e 100.")
    print(f"Você tem {tentativas_totais} tentativas para adivinhar!\n")

    while tentativas < tentativas_totais:
        palpite = input(f"Tentativa {tentativas + 1}. Digite seu palpite: ")

        if not palpite.isdigit():
            print("Entrada inválida! Por favor, digite um número inteiro entre 1 e 100.")
            continue
        palpite = int(palpite)
        if palpite < 1 or palpite > 100:
            print("O número está entre 1 e 100.")
            continue
        if palpite in palpites_feitos:
            print("Você já tentou esse número. Tente outro.")
            continue

        palpites_feitos.append(palpite)
        tentativas += 1

        if palpite == numero_secreto:
            print(f"\nParabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontos = (tentativas_totais - tentativas + 1) * 10 * int(dificuldade)  # pontuação decrescente conforme erra
            return pontos

        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")

        print(f"Tentativas restantes: {tentativas_totais - tentativas}")
        print(f"Palpites já feitos: {palpites_feitos}")

    print(f"\nQue pena! Suas tentativas acabaram. O número era {numero_secreto}.")
    return 0

# Placar total
pontuacoes = []

while True:
    pontos = jogar_adivinhacao()
    pontuacoes.append(pontos)

    # Exibe Placar Atual
    print("\nPlacar:")
    for idx, pts in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pts} pontos")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima!")
        break

