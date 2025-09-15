#funções foram criadas para não precisar repetir ou reescrever códigos.
# def: Indica que estamos definido uma função
# nome_da_funcao: Nome que escolhemos para a função
# ():: Parênteses que podem conter parâmetros
# pass: Palavra-chave usada como placeholder quando não há código dentro da função

def saudacao():
    print("Olá! Seja bem-vindo!")

saudacao()

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")
saudacao("Maria")

def apresentar_pessoa(nome,idade):
    print(f"Esta é {nome}, e ela tem {idade} anos.")
apresentar_pessoa("João",30)

def saudacao(nome, mensagem="Seja bem-vindo"):
    print(f"Olá, {nome}! {mensagem}")
saudacao("Ana")

def soma(a,b):
    resultado = a + b
    return resultado
total = soma(5,3)
print("O Total é: ",total)

def multiplicar(a,b):
    produto = a * b
    return produto
resultado = multiplicar(4,5)
print("Resultado: ",resultado)

mensagem_global = "Olá, mundo!"
def exibir_mensagem():
    print(mensagem_global)
exibir_mensagem()

def calcular_area():
    largura = 5
    altura = 3
    area = largura * altura
    print("Àrea: ",area)
calcular_area

numero = 10
def mostrar_numero():
    numero = 5
    print("Número dentro da função: ",numero)
mostrar_numero()
print("Número fora da função: ",numero)

contador = 0
def incrementar():
    global contador
    contador +=1

incrementar()
print("Contador: ",contador)

def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!" 
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+,-,*,/): ")

if operacao == '+':
    resultado = somar(numero1,numero2)
elif operacao == '-':
    resultado = subtrair(numero1,numero2)
elif operacao == '*':
    resultado = multiplicar(numero1,numero2)
elif operacao == '/':
    resultado = dividir(numero1,numero2)
else:
    resultado = "Operação Inválida!"
print("Resultado: ",resultado)

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True
num = int(input("Digite um número inteiro: "))
if eh_primo(num):
    print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

def celsius_para_fahrenheit(c):
    return c * 9/5 +32
def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9
def celsius_para_kelvin(c):
    return c + 273.15
def kelvin_para_celsius(k):
    return k - 273.15
temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade atual (C,F,K): ").upper()
converter_para = input("Converter para (C,F,K): ").upper()

if unidade == "C":
    if converter_para == "F":
        resultado = celsius_para_fahrenheit(temperatura)
    elif converter_para == "K":
        resultado = celsius_para_kelvin(temperatura) 
elif unidade = "F":
    if converter_para == "C":
        resultado = fahrenheit_para_celsius(temperatura)
    elif converter_para == "K":
        celsius = fahrenheit_para_celsius(temperatura)
        resultado = celsius_para_kelvin(celsius)
elif unidade == "K":
    if converter_para == "C":
        resultado = kelvin_para_celsius(temperatura)
    elif converter_para == "F":
        celsius = kelvin_para_celsius(temperatura)
        resultado = celsius_para_fahrenheit(celsius)
else:
    resultado = "Unidade inválida."
print(f"Temperatura convertida: {resultado} {converter_para}")

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
num = int(input("Digite um número inteiro positivo: "))
if num => 0:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}.")
else:
    print("Número inválido.")
