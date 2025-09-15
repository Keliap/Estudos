def divisao_segura():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")
    else:
        print(f"Resultado da divisão: {resultado}")
        
divisao_segura()