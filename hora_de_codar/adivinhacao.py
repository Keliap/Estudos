import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação:")
    print("Tente adivinhar o número de 1 a 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        else:
            print("Muito alto! Tente novamente.")
jogo_adivinhacao()
