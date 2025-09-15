def ler_arquivo(nome_arquivo):
    """
    Lê o conteúdo de um arquivo e retorna uma lista com as linhas do arquivo.
    
    :param nome_arquivo: O caminho do arquivo a ser lido.
    :return: Lista contendo as linhas do arquivo.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except PermissionError:
        print("Erro: Permissão negada para ler o arquivo.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
ler_arquivo('dados.txt')