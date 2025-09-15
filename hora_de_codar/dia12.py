#tratamento de exceção
#try: Código que pode gerar exceção
#except: Código que será executado se ocorrer uma exceção
#finally: Código que será executado sempre, independentemente de ocorrer ou não uma exceção
#else: Código que será executado se não ocorrer uma exceção
try:
    texto = input("Digite um texto: ")

    contagem = {}
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    print("Contagem de caracteres: ")
    for caractere, quantidade in contagem.items():
        print(f"'{caractere}': '{quantidade}'")
except Exception as e:
    print(f"Ocorreu um erro: {e}") 
# Código que será executado sempre, independentemente de ocorrer ou não uma exceção
finally:
    print("Programa finalizado.")   
try:
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
except  FileNotFoundError:
    print("Erro O arquivo 'dados.txt' não foi encontrado.")
else:
    print("Arquivo lido com sucesso.")
    print(conteudo)    
finally:    
    print("Operção de leitura de arquivo finalizada")
try:
    numero = int(input("Digite um número: "))  
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"Número digitado: {numero}")
finally:
    print("Operação de entrada de número finalizada.")

    #O bloco else é opcional e é executado se não ocorrer nenhuma exceção no bloco try.

try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado da divisão: {resultado}")

# O bloco finally é opcional e é executado sempre, independentemente de ocorrer ou não uma exceção.

