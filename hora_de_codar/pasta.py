import os

def pasta():
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada")

    os.chdir('nova_pasta')

    with open('arquivo.txt','w') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta.")
    print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'. ")
    
    arquivo = os.listdir('.')
    print("Arquivos no diretório atual: ", arquivo)
pasta()