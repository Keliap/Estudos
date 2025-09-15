frase = input("Digite uma frase: ")
palavras = frase.split()
frase_invertida = " ".join(reversed(palavras))
print(f"A frase invertida: {frase_invertida}")