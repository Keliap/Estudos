import math
from math import sqrt, pi
import math as m
import random
from datetime import datetime
import os 
import meu_modulo
import requests

numero = 16
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada do {numero} é {raiz_quadrada}")
print(f"O valor de pi é {pi}")
print(f"A raz quadrada de 25 é {sqrt(25)}")
print(f"Cosseno de 0 é {m.cos(0)}")

dado = random.randint(1,10)
print(f"O resultado do dado é: {dado}")

agora = datetime.now()
print(f"Data e hora atuais: {agora}")

arquivos = os.listdir('.')
print("Arquivos diretórios atual: {arquivos}")

mensagem = meu_modulo.saudacao("Kélia")
print(mensagem)

resultado = meu_modulo.soma(5,9)
print(f"A soma é {resultado}")

respostas = requests.get('https://api.github.com/')
print(f"Status da reposta: {respostas.status_code}")

