arquivo = open('dados.txt','r')
conteudo = arquivo.read()
print(conteudo)
linha = arquivo.readline()
while linha:
    print(linha.strip())
    linha = arquivo.readline()
arquivo.close()

linhas = arquivo.readlines()
for linha in linhas:
    print(linha.strip())
