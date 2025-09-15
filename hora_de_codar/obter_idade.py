def obter_idade():
    while True:
        try:
            idade = int(input("Por favor, insira sua idade: "))
            if idade < 0:
                raise ValueError("Idade não pode ser negativa.")
            return idade
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para a idade.")
idade_usuario = obter_idade()
print(f"Sua idade é: {idade_usuario}")