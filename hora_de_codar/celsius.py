def celsius_para_fahrenheit(celsius):
    try:    
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahreinheit = (celsius * 9/5) + 32
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira um número válido.")
    else:
        print(f"{celsius} graus Celsius é igual a {fahreinheit} graus Fahrenheit.")
celsius_para_fahrenheit(0)