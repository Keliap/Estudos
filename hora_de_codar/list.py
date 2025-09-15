lista = ['maça','banana','laranja']

def acessar_elemento():
    try:
        indice = int(input("Digite um indice: "))
        elemento = lista[indice]
    except ValueError:
        print("Erro: Por favor, insira um número inteiro")
    except IndexError:
        print("Erro: Índice fora do intervalo da lista.")
    else:
        print(f"Elemento no índice {indice}: {elemento}")
acessar_elemento()