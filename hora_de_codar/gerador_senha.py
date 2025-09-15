import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + strings.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for_in range(tamanho))
    return senha
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print("Senha gerada: ", senha_gerada)