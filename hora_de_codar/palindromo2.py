palavra = input("Digite uma palavra: ").lower()
palavra_sem_espaco = palavra.replace(" "," ")
if palavra_sem_espaco == palavra_sem_espaco [::-1]:
    print("É um palindromo")
else:
    print("Não é palindromo")