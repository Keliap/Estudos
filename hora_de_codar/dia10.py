frase1 = 'Olá, mundo'
frase2 = 'Estou aprendendo python'
#strings são frases ou palavras que tenho que escrever dentro de aspas simples ou duplas

#para concantenar uma strings, eu uso o +.

saudacao = 'Olá! '
mensagem = 'Seja muito bem-vinda ao mundo de programação'
resultado = saudacao + mensagem
print(resultado)

#primeiro precisa de variaveis para guardar informações na memória, tudo funciona em 
#programação com variáveis.

#O programa é burro e você é quem tem pensar e orientar passo a passo, as informações do mundo real
#para o mundo abstrato.
#Tenho que pensar e imaginar e não ficar dependendo das pessoas 
#Agir com base na minha fé, use a cabeça.
#Não adianta ter teoria, sem prática. Para ser excelente profissional preciso depender de
#Deus e práticar. Não posso enterrar o talento que Deus me deu.

#Para repetir uma string preciso usar o asterico

risadas = "ha" * 3
print(risadas)
#Eu realmente entendendo o que é programação? Ou lógica de programação?
#E como devo aplicar ela no dia a dia?

#Estou aprendendo a como programar e não sentir. Usar a cabeça e não o coração.

palavra = 'python'
primeira_palavra = palavra[0]
print(primeira_palavra)

palavra = 'programação'
fatia = palavra[0:2]
print(fatia)
#em fatiamento o indice final não pega o objeto atrelado a ele e sim um anterior.
#exemplo uma lista ou array que tenha cinco elementos de 0 a 5, na verdade tem 6. 
#Porque o zero conta como o primeiro elemento,então se for utilizar um fatiamento [0:5],
#ele na verdade, vai pegar os quatros elementos. Ou seja, não é como o array e que pegar as
#seis posições, ele vai pegar b-1, no caso de fatiamento de string.

#para saber o comprimento da string, usa-se o len. Ou lenght.

texto = "Aprendendo python"
tamanho = len(texto)
print(f"O texto tem {tamanho} caracteres")
#o espaço em branco é um caracter

#metódo format

idade = 25
mensagem = "Kélia tem {} anos".format(idade)
print(mensagem)

nome = 'Kélia'
cidade = 'Belo Horizonte'
mensagem = f"Me chamo {nome} e moro em {cidade}"
print(mensagem)

#maíusculas e minúsculas

texto = 'boa tarde'
print(texto.upper())
print(texto.lower())
print(texto.title())
#title somente as palavras iniciais da frase é colocada em maiúsculas

#o strip remove espaços em branco

texto = '    olá'
print(texto.strip())

#replace troca uma palavra na frase

frase = "Estou aprendendo python"
nova_frase = frase.replace("python","Java")
print(nova_frase)

#find é usado para encontrar a posiçao de uma substring

frase = "Onde está o Wally"
posicao = frase.find("Wally")
print(f"Wally está na posição {posicao}")

# O split a string em uma lista, usando um separador.

dados = "maça,banana,laranja"
lista_frutas = dados.split(",")
print(lista_frutas)

#O join junta os elmentos de uma lista em uma string

lista_palavras = ["Python","é","legal"]
frase = ' '.join(lista_palavras)
print(lista_palavras)


