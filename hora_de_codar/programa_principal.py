import conversoes

temperatura_c = float(input("Digite a temperatura em celsius: "))
temperatura_f = conversoes.celsius_para_fahrenheit(temperatura_c)
temperatura_k = conversoes.celsius_para_kelvin(temperatura_c)
print(f"{temperatura_c}°celsius equivalem a {temperatura_f}°f e {temperatura_k}°k")