def ler_arquivo_usuario():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
    except  FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")  
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o arquivo '{nome_arquivo}'.")   
    except Exception as e:
        print(f"Erro inesperado: {e}")
ler_arquivo_usuario()
