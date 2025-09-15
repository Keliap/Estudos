import random

pontuaçoes = []

while True:
    numero_secreto = random.randint(1,100)
    tentativas_restantes = tentativas_totais
    tentativas = 0
    palpites_feito = []

print(f"\nEu pensei em um número entre 1 e 100.")
print(f"\nVocê tem {tentativas_totais} tentativas para adivinhar.")

#loop de tentativas
while tentativas_restantes > 0:
    palpite = input("\nDigite seu palpite")

    #verificando se o input é um número válido
    if not palpite.isdigit():
        print("Entrada inválida! Por favor, digite um número inteiro entre 1 e 100")
        continue
    palpite = int(palpite)
    if palpite < 1 or  palpite > 100:
        print("O número está entre 1 e 100.")
        continue
    if palpite in palpites_feito:
        print("Você já tentou esse número. Tente outro.")
        continue
    else:
        palpites_feito.append(palpite)

        tentativas += 1
        tentativas_restantes -= 1
    if palpite == numero_secreto:
        print(f"\nParabéns! Você acertou o número em {tentativas} tentativa(s).")
        pontuacao = tentativas_restantes * 10 * int(dificuldade)
        pontuaçoes.append(pontuacao)
        print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
        break
    elif palpite < numero_secreto:
        print("O número é maior que esse.")
    else:
        print("O número é menor que esse.")
    
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Palpites já feitos: {palpites_feito}")

else:
    print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}")
    pontuaçoes.append(0)
#Exibindo o placar 

print("\nPlacar:")

for idx, pontos in enumerate(pontuaçoes, start=1):
    print(f"Partida {idx}: {pontos} pontos")

#perguntar se o jogador quer jogar novamente
jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
if jogar_novamente != 's':
    print("Obrigado por jogar! Até a próxima")
    Break