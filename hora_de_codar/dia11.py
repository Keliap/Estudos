#Dicionários em python não são iguais a um json, mesmo que a sintaxe seja a mesma.
#Eles são parecidos, porém não são os mesmos, porque json é dados estruturados para banco de dados
#já dicionários é um objeto na memória.

frutas= ["maça", "banana", "maça", "banana"]
frutas_unicas = set(frutas)
print(frutas_unicas)

#Criando um dicionário
#É parecido com a criação de um objeto json

aluno = {
    "nome": "Kélia",
    "idade": "39",
    "curso": "tecnologia"
}
#Para acessar os valores da chaves, é necessário utilizar colchetes.

print(aluno["nome"])
#Para adicionar um novo par de chave e valor usa-se aluno["nota"]=9.5

aluno["nota"] = 9.5
#atulizando um valor existente
aluno["idade"] = 21
#removendo itens, utilizando del
del aluno["curso"]
idade = aluno.pop("idade")
print(idade)

#para percorrer um dicionário
for chave, valor in aluno. items():
    print(f"{chave}: {valor}")

#Trabalhando com conjuntos - Criando um conjunto:
numeros={1,2,3,5,6,7}
#transformar uma lista em conjunto:
lista = [1,2,2,4,4,6,1]
numeros_unicos = set(lista)
numeros.add(8)
numeros.remove(8)
print(numeros_unicos)
#adicionando e removendo elementos
#adicionando 
numeros.add(6)
#removendo
numeros.remove(1)
print(numeros)

#operação com conjuntos
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}
uniao = conjunto_a.union(conjunto_b)
print(uniao)

#interseção

intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

#diferença
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)


