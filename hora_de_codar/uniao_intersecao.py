numeros1 = input("Digite números separados por espaço para o primeiro conjunto: ").split()
numeros2 = input("Digite números separados por espaço para o segundo conjunto: ").split()

conjuntos1 = set(numeros1)
conjuntos2 = set(numeros2)

uniao = conjuntos1.union(conjuntos2)
intersecao = conjuntos1.intersection(conjuntos2)

print("União dos conjuntos: ", uniao)
print("Interseção dos conjuntos: ", intersecao)
