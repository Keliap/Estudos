nome_arquivo = input("Digite o nome do arquivo: ")
contagem = {}
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
else:
    palavras = conteudo.lower().split()
    
    for palavra in palavras:
        palavras = palavra.strip('.,!?";:-()')
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
for palavra, quantidade in contagem.items():
    print(f"{palavra}:{quantidade}")
       
        