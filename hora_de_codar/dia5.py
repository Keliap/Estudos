
#estrutura de repetição

#repetir n vezes
#Onde o n, a gente pode definir
#ou n é uma condição

frutas = ["maça", "Banana", "Laranja"]
for frutas in frutas:
    print("Eu gosto de",frutas)

for i in range(5): # o comando range gera números de 0 a 4 e exclui o 5, isso significa que 
    print("Número: ") #toda a vez que usar esse comando tem que saber dessa regra.
    
#while
# O while repete enquanto a condição for verdadeira
contador = 0

while contador < 5:
    print("Contagem ",contador)
    contador +=1 # Esse comando equivale a adicionar mais um número na contagem

#O break é usado para interromper uma condição imediatamente, mesmo que ela seja verdadeira.
for numero in range(10):
    if numero == 5:
        break
    print("Número ",numero)
#Já o continue pula para a próxima iteração ou condição

for numero in range(5):
    if numero == 2:
        continue
    print("Número: ", numero)

for numero in range(1,11):
    print(numero)

n = int(input("Digite um número inteiro positivo: "))
soma = 0


for i in range(1,n):
    soma += 1
print("A soma dos números de 1 a ", n,"é", soma)

numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

pares = 0
impares = 0

for numero in range(1,21):
    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1
print("Quantidade de pares: ", pares)
print("Quantidade ímpares: ", impares)

import random

numero_secreto = random.randint(1,100)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    break
if palpite == numero_secreto:
    print(f"Parabéns! Você acertou em {tentativas} tentativas.")

elif palpite < numero_secreto:
    print("O número é maior")
else:
    print("O número é menor")

N = int(input("Digite um número inteiro positivo"))
fatorial = 1

if N < 0:
    print("Não existe fatorial de número negativo.")
elif N ==0 or N == 1:
    print(f"O fatorial de {N} é 1")
else:
    for i in range(1, N+1):
        fatorial *= i
print(f"O fatorial de {N} é {fatorial}")

n = int(input("Quantos termos da série Fibonacci você quer? "))

termo1 = 0
termo2 = 1
contador = 0

if n <= 0:
    print("Por favor, insira um número positivo. ")
elif n == 1:
    print("Serie fibonacci até", n, "termo")
    print(termo1)
else:
    print ("Série Fibonacci:")
    while contador < n:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1


    
palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print("Palavra:"," ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
            print("Boa! Você acertou uma letra")
        else:
            tentativas -= 1
            print(f"Errou!Você tem {tentativas} tentativas restantes.")
    if "_" not in letras_descobertas:
        print("Parabéns! Você adivinhou a palavra: ", palavra_secreta)
    else:
        print("Você perdeu! A palavra era: ", palavra_secreta)
        