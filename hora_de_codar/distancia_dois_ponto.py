import numpy

def distancia(ponto1, ponto2):
    x1, y2 = ponto1
    x2, y2 = ponto2
    return numpy.sqrt((x2 - x1)**2 + (y2 - y1)**2)
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

dist = distancia((x1, y1),(x2, y2))
print(f"A distância entre os pontos é: {dist}")