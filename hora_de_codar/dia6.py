frutas = ["maçã","Morango","Acerola"]
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas)
frutas.append("Uva")
print(frutas)
frutas.insert(2,"Abacaxi")
print(frutas)
frutas.remove("Abacaxi")
print(frutas)
frutas.pop()
print(frutas)
print(len(frutas))
if "maçã" in frutas:
    print("Maçã está na lista")

numeros = [1,2,3,4,5,7,8,9]
numeros.append(6)
numeros[0] = 10
numeros.remove(3)
print(numeros)

cores = ("Vermelho","Azul","Verde")
print(cores[1])

listas_frutas = ["maçã","banana","laranja"]
tupla_frutas = tuple(listas_frutas)
print(tupla_frutas)

listas_cores = list(cores)
print(listas_cores)

frutas = ["Maçã","Banana","Laranja"]
for fruta in frutas:
    print("Eu gosto de você", fruta)

for i in range(len(frutas)):
    print(f"Fruta na posição {i}: {frutas[i]}")

cores = ("Vermelho","Azul","Verde")

for cor in cores:
    print("A cor é", cor)

frutas = ["Maçã","Banana","Laranja"]

for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")

convidados = ["Ana","Bruno","Carlos","Diana"]
for convidado in convidados:
    print(f"Olá, {convidado}! Você está convidado para a festa")

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numero = sum(numeros)
media_numero = soma_numero / len(numeros)

print("Maior número: ", maior_numero)
print("Menor número: ", menor_numero)
print("Soma dos números: ", soma_numero)
print("Média dos números: ",media_numero)


frase = input("Digite uma frase: ").lower()
letras = {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1
for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]
numeros_crescente = sorted(numeros)
print("Números em ordem crescente: ",numeros_crescente)
numeros_decrescente = sorted(numeros, reverse=True)
print("Números em ordem decrescente: ", numeros_decrescente)

meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto",
         "Setembro","Outubro","Novembro","Dezembro")
numero_mes = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero_mes <=12:
    print(f"O mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 12.")

tarefas = []

while True:
    print("\nMenu de tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefas)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso.")
        else:
            print("Tarefa não encontrada")
    elif opcao == 3:
        print("\nLista de tarefas:")
        for idx,tarefa in enumerate(tarefas,start=1):
            print(f"{idx}.{tarefa}")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

notas = []

while True:
    entrada = input("Digite uma nota (ou 'sair' para finalizar):")
    if entrada.lower() == 'sair':
        break
    else:
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    if notas:
            maior_nota = max(notas)
            menor_nota = min(notas)
            media = sum(notas) / len(notas)
            notas_acima_media = [nota for nota in notas if nota > media]

            print("\nResultados: ")
            print("Maior nota: ", maior_nota)
            print("Menor nota: ",menor_nota)
            print("Média da turma: ", media)
            print("Nota acima da média: ", notas_acima_media)
    else:
        print("Nenhuma nota foi inserida.")

texto = input("Digite um texto: ").lower()
palavras =texto.split()
contagem_palavra = {}

for palavra in palavras:
    if palavra in contagem_palavra:
        contagem_palavra[palavra] += 1
    else:
        contagem_palavra[palavra] = 1
print("\nContagem de palavras: ")
for palavra, contagem in contagem_palavra.items():
    print(f"A palavra '{palavra}' aparece '{contagem}' vez(es).")

